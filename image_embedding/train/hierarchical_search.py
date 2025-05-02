import sys
from qdrant_client import QdrantClient
from embedding_model import get_embedding  # Görselden embedding çıkarma fonksiyonu
from qdrant_client.http import models  # Qdrant modelleri için gerekli


COLLECTION_NAME = "sutas_icim_embed_mean_hierarchical_embeddgin"  # Qdrant koleksiyon adı

# Qdrant bağlantısı
client = QdrantClient(host="localhost", port=6333)

from qdrant_client.http import models  # Qdrant modelleri için gerekli

def hierarchical_search(image_path, top_k=1):
    # Görselden embedding çıkar
    vector = get_embedding(image_path)

    # 1. Seviye: Markalar arasında arama
    brand_results = client.scroll(
        collection_name=COLLECTION_NAME,
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="brand",
                    match=models.MatchValue(value="İçim")  # Marka filtresi
                )
            ]
        ),
        limit=top_k,
        with_payload=True
    )

    if not brand_results:
        print("Hiçbir marka bulunamadı.")
        return

    # En yüksek doğruluk oranına sahip markayı seç
    best_brand = brand_results[0].payload["brand"]
    print(f"En iyi eşleşen marka: {best_brand}")

    # 2. Seviye: Kategoriler arasında arama
    category_results = client.scroll(
        collection_name=COLLECTION_NAME,
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="brand",
                    match=models.MatchValue(value=best_brand)  # Seçilen markaya göre filtrele
                ),
                models.FieldCondition(
                    key="categories.name",
                    match=models.MatchValue(value="Puding")  # Kategori filtresi
                )
            ]
        ),
        limit=top_k,
        with_payload=True
    )

    if not category_results:
        print(f"{best_brand} markası için hiçbir kategori bulunamadı.")
        return

    # En yüksek doğruluk oranına sahip kategoriyi seç
    best_category = category_results[0].payload["categories"][0]["name"]
    print(f"En iyi eşleşen kategori: {best_category}")

    # 3. Seviye: Alt kategoriler arasında arama
    subcategory_results = client.scroll(
        collection_name=COLLECTION_NAME,
        scroll_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="brand",
                    match=models.MatchValue(value=best_brand)  # Seçilen markaya göre filtrele
                ),
                models.FieldCondition(
                    key="categories.name",
                    match=models.MatchValue(value=best_category)  # Seçilen kategoriye göre filtrele
                ),
                models.FieldCondition(
                    key="categories.subcategories.name",
                    match=models.MatchValue(value="Icim-Dolcia-Cikolatali-Puding-60g")  # Alt kategori filtresi
                )
            ]
        ),
        limit=top_k,
        with_payload=True
    )

    if not subcategory_results:
        print(f"{best_brand} markası ve {best_category} kategorisi için hiçbir alt kategori bulunamadı.")
        return

    # En yüksek doğruluk oranına sahip alt kategoriyi seç
    best_subcategory = subcategory_results[0].payload["categories"][0]["subcategories"][0]["name"]
    print(f"En iyi eşleşen alt kategori: {best_subcategory}")

    # Sonuçları yazdır
    print("----------")
    print(f"Marka: {best_brand}")
    print(f"Kategori: {best_category}")
    print(f"Alt Kategori: {best_subcategory}")
    print(f"Benzerlik Skoru: {subcategory_results[0].score:.4f}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python hierarchical_search.py path/to/image.jpg")
    else:
        image_path = sys.argv[1]
        hierarchical_search(image_path)