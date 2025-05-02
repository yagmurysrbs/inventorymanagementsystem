# import sys
# from qdrant_client import QdrantClient
# from embedding_model import get_embedding  # embedding çıkarma fonksiyonu

# COLLECTION_NAME = "sutas_icim_embed_mean"  # Qdrant koleksiyon adı

# # Qdrant bağlantısı
# client = QdrantClient(host="localhost", port=6333)

# def search_similar_image(image_path, top_k=1):
#     # Görselden embedding çıkar
#     vector = get_embedding(image_path)

#     # Eski API için doğru parametre: limit
#     hits = client.search(
#         collection_name=COLLECTION_NAME,
#         query_vector=vector,
#         limit=top_k,               # En yakın 1 sonucu al
#         with_payload=True
#     )

#     for hit in hits:
#         print(f" Benzer skor: {hit.score:.4f}")
#         print(f" Eşleşen ürün ID: {hit.id}")
#         print(f" Ek bilgiler: {hit.payload}")
#         print("----------")


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Kullanım: python qdrant_search.py path/to/image.jpg")
#     else:
#         image_path = sys.argv[1]
#         search_similar_image(image_path)

"""
    [0.020321507,-0.12598318,-0.07832449,0.10618875,0.01305609,0.006753593,0.03658858,0.03178313,0.017371092,0.003760672,-0.019105747,-0.03553416,0.018862024,-0.013019346,-0.022289213,0.03171404,-0.08172461,0.03467177,0.054114114,0.091163106,0.01853738,0.03870047,0.0041471543,0.029188693,-0.041958258,-0.041355383,0.018528359,-0.0013912405,-0.022172328,-0.04154583,-0.0037690317,0.0011053989,0.037865255,0.0074005933,-0.02120502,0.045647047,-0.03832067,0.017928759,0.002900489,0.009665125,-0.0012489181,0.0033906677,-0.055872545,0.041991744,0.083780184,-0.026768269,-0.069591336,-0.05383607,-0.032335747,-0.030356418,-0.004318396,-0.02698476,-0.031681363,-0.007258513,-0.09760138,-0.008608736,-0.066905834,0.024554586,0.032008022,0.02952882,0.00096678775,-0.096758924,0.07605633,-0.02098874,-0.019354036,-0.015991336,0.014602806,0.05585648,0.041410927,0.075936936,-0.05737824,-0.08114678,-0.03973918,0.04567118,0.065213904,-0.006614529,-0.15626909,0.013926913,0.027995976,-0.025362989,0.0035809036,-0.011148303,0.006675367,0.001931843,-0.0030752623,-0.05339393,0.02979539,-0.020283451,0.0045140763,-0.030475656,0.06411074,0.0069833193,0.007470495,0.017427104,-0.076778695,-0.0069873245,-0.028619746,0.07372342,-0.072514035,0.0256065,0.018062642,0.017532038,0.007440296,-0.009693472,0.009450974,0.017305318,-0.028640036,0.13908686,-0.0013516071,0.0252615,-0.029806282,0.06441657,0.026478512,0.04782382,0.011556239,-0.039222907,-0.010151214,0.031054698,-0.09124769,0.017961523,-0.0460538,0.015795255,-0.034764558,0.063737705,-0.04009051,-0.077363364,0.082844846,-0.0042345366,0.018839387,0.021961479,0.012137254,0.05429643,-0.038705677,0.002804593,-0.019549645,-0.043610748,-0.017792169,0.0055266675,0.019374497,-0.0060473955,-0.027983122,0.04634801,0.072730936,-0.038988642,-0.017081978,-0.07746622,0.013863704,0.034267396,-0.030167768,-0.014341013,-0.0020723876,0.09850807,0.13572256,0.048126005,-0.04329964,0.057877574,0.009644928,0.015509348,-0.0011632058,-0.056224726,0.008812307,0.0053563025,-0.02489938,0.045281652,0.05254346,0.061215967,-0.016442008,-0.00842964,0.05961254,-0.005038602,-0.06988093,0.022015665,0.02608153,0.009387374,-0.02408907,0.15311155,-0.037564766,0.032806255,-0.16754822,0.0061263237,0.001910315,-0.047538564,0.0053083855,0.04170591,-0.0022071765,-0.015644263,-0.052698612,0.01690269,0.042544607,-0.035928395,-0.0039230045,0.08589588,0.02743592,0.007908133,0.045465935,-0.0053987587,0.0010951966,-0.033583708,-0.032994818,-0.043161348,-0.075228855,0.031433526,0.025042035,0.011339305,0.04165513,0.022044878,0.071477436,-0.04443861,-0.022508992,-0.036326945,0.043891255,0.08664771,0.043639928,-0.10477564,0.022313247,0.011403708,-0.011459788,0.032205015,0.02246137,-0.019885352,0.0044206223,0.00022753385,-0.022486359,0.0026120434,0.024689687,-0.043536592,0.06704386,0.02738778,-0.04635211,-0.005836685,0.025313923,0.0020757644,-0.048468705,0.037790608,0.057238147,0.06415514,-0.030273065,0.033338875,0.06188367,0.05524517,0.0002475973,0.096066765,0.041533712,-0.0076376256,-0.029525425,-0.056652203,0.02437848,0.0008863144,0.030444423,0.0071378704,0.02467593,0.056737576,-0.0087427795,-0.05737466,-0.027457688,-0.013200872,-0.02664538,-0.07526291,-0.0028054873,-0.0009430386,0.045987286,-0.0049085044,0.015477154,0.053502247,-0.012101513,-0.057721116,-0.006374652,-0.009574705,0.047388416,-0.07153712,-0.028565332,-0.05585701,0.04931784,-0.01601367,-0.034004238,0.0021150375,0.05185172,0.01838542,-0.025603019,-0.06817006,-0.020936085,-0.01011192,-0.049714956,0.034585983,-0.025172656,0.0057149567,-0.05311763,0.024282219,0.039067637,0.0036832727,0.012254246,0.03948708,-0.0013271257,-0.02066277,0.01485543,-0.0032490043,-0.090552785,-0.00039719284,-0.014826897,0.017470945,-0.01767779,0.014498597,-0.041420247,-0.09343397,-0.06476405,-0.0842416,0.017270165,-0.13558912,-0.015219982,-0.065910615,0.010966527,0.06086987,0.014073896,0.07071192,0.022270486,-0.015250032,-0.034210198,-0.05299399,-0.04259912,-0.02448398,-0.046082146,0.010637146,0.024816798,0.05172733,-0.077341355,-0.097845934,-0.009895669,0.06509287,0.010511327,-0.020243196,-0.026543617,0.04218847,-0.02253245,0.10390915,0.012634081,-0.043300197,-0.03615502,0.020034602,0.015445899,-0.01548318,0.0438517,0.007832244,0.057542857,0.013187745,0.01124215,0.0014191607,0.019232497,0.017036911,-0.10707807,-0.056998502,-0.024301011,-0.057969097,-0.011260614,0.03321932,-0.081163496,-0.016656911,0.0036639979,0.012783596,-0.040146135,-0.00882649,0.05682963,0.04070217,-0.016042536,0.05726211,-0.04533788,0.005591041,-0.0046945075,0.05575418,-0.08452976,-0.005591403,-0.000010406988,0.012389774,0.01032791,0.017890632,0.004264766,0.041144866,0.021459367,0.056721553,-0.016189424,-0.019624956,0.0068233334,0.005822706,0.012694494,0.013427217,0.02089672,0.0417488,-0.018657692,-0.051693346,0.008365415,-0.004153668,0.026543984,-0.01992327,-0.0025912912,0.0045964997,0.022447683,-0.046844646,-0.049581256,-0.02999358,0.020545792,0.057407398,0.01970766,0.047115322,0.036470894,0.008058637,0.0029520087,0.026185026,-0.02714546,-0.070919886,-0.0063469335,0.02781122,0.051549453,0.033480324,0.030049473,-0.05429824,-0.0052956375,0.022381686,0.01908562,0.036085524,0.02323647,-0.032042526,-0.0035854655,-0.038477812,-0.03166993,0.02338854,0.006336417,-0.007773963,-0.032493494,-0.03735844,-0.03043142,-0.019603496,-0.019609392,0.032617617,0.030468933,-0.017160296,-0.005102923,0.04065267,-0.02760875,0.011460646,0.037292678,-0.004629566,0.009785583,-0.010257085,-0.011261624,-0.04263795,-0.09041075,0.0024960525,-0.016233543,-0.0022308512,0.009655919,-0.022816341,0.02054353,0.047969,0.07425186,-0.018453378,-0.06464546,-0.11071943,0.005897957,-0.0489225,0.066401236,-0.045850575,0.0059555653,-0.07237248,0.022191565,-0.061211567,-0.03932146,0.06305265,0.007971095,-0.0002781067,0.044499505,-0.05749301,-0.060499065,0.09366909,0.01371509,0.011755236,-0.013320202,0.06784692,0.010953849,0.0400399,-0.056916274,-0.020533683,0.028982924,-0.08091635,-0.038000576,0.077284455,0.094308384,-0.0069333524,0.10692213,0.016919648,-0.05745301,0.00096283806,0.02536714,-0.0003272645,0.09324754,0.006656763,0.047393296,0.06980263,-0.10125209,-0.0030293162,-0.049230985,-0.015111106,-0.026060272,0.006308139,-0.025561359,-0.008654604,-0.0698199,0.038420428,0.05301749,0.073470645,-0.017596034,0.013856785,0.036212288,-0.059549294]
"""



"""
    search hiyerar...
"""

# import numpy as np
# from PIL import Image
# import torch
# from transformers import CLIPProcessor, CLIPModel
# from qdrant_client import QdrantClient

# # CLIP modelini yükle
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip").to(device)
# processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

# def get_image_embedding_only(image_path):
#     """
#     Sadece görselden embedding çıkarır (text olmadan).
#     """
#     try:
#         image = Image.open(image_path).convert("RGB")
#         inputs = processor(images=image, return_tensors="pt").to(device)
#         with torch.no_grad():
#             outputs = model.get_image_features(**inputs)
#         return outputs[0].cpu().numpy().astype("float32")
#     except Exception as e:
#         print(f"Hata (embedding çıkarma): {e}")
#         raise

# def search_image_hierarchy(image_path, collection_name, client: QdrantClient):
#     """
#     Sadece görsel verilerek Qdrant içinde en yakın ürünü arar.
#     """
#     try:
#         query_vector = get_image_embedding_only(image_path)
#     except Exception as e:
#         print(f"Embedding çıkarılırken hata oluştu: {e}")
#         return None

#     try:
#         results = client.search(
#             collection_name=collection_name,
#             query_vector=query_vector.tolist(),
#             limit=1,
#             with_payload=True
#         )
#     except Exception as e:
#         print(f"Qdrant arama hatası: {e}")
#         return None

#     if not results:
#         return None

#     result = results[0]
#     payload = result.payload
#     score = result.score
#     similarity_percent = round(score * 100, 2)

#     return {
#         "product_name": payload.get("product_name", "Bilinmiyor"),
#         "categories": payload.get("categories", []),
#         "similarity_percent": similarity_percent
#     }

# # Örnek kullanım
# if __name__ == "__main__":
#     client = QdrantClient(host="localhost", port=6333)
#     collection_name = "sutas_icim_hierarchical"
#     image_path = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Gıda/icim/Peynir/SüzmePeynir/icim-tag-yagli-peynir-500Gr.jpg" 

#     result = search_image_hierarchy(image_path, collection_name, client)

#     if result:
#         print("✅ Tahmin edilen ürün:", result["product_name"])
#         print("📁 Kategori yapısı:", " > ".join(result["categories"]))
#         print("🎯 Benzerlik oranı:", f"%{result['similarity_percent']}")
#     else:
#         print("❌ Benzer ürün bulunamadı.")



"""
    tree search
"""

# import sys
# from qdrant_client import QdrantClient
# from embedding_model import get_embedding  # embedding çıkarma fonksiyonu


# COLLECTION_NAME_MarkaCollection = "MarkaCollection"  
# COLLECTION_NAME_icimSutUrunleriCollection = "icimSutUrunleriCollection"  
# COLLECTION_NAME_sutasSutUrunleriCollection = "sutasSutUrunleriCollection"  
# COLLECTION_NAME_icimPeynirCollection = "icimPeynirCollection"  
# COLLECTION_NAME_icimPudingCollection = "icimPudingCollection"  
# COLLECTION_NAME_icimSutCollection = "MarkaCollecicimSutCollectiontion"  
# COLLECTION_NAME_sutasPeynirCollection = "sutasPeynirCollection"  
# COLLECTION_NAME_sutasPudingCollection = "sutasPudingCollection"
# COLLECTION_NAME_sutasSutCollection = "sutasSutCollection"   

# # Qdrant bağlantısı
# client = QdrantClient(host="localhost", port=6333)

# def search_similar_image(image_path):
#     # Görselden embedding çıkar
#     vector = get_embedding(image_path)

#     # Koleksiyondaki toplam vektör sayısını al
#     collection_info = client.get_collection(COLLECTION_NAME_MarkaCollection)
#     total_points = collection_info.points_count

#     if total_points is None or total_points == 0:
#         print("Koleksiyonda hiç vektör yok.")
#         return

#     # Hepsiyle karşılaştırma yap
#     hits = client.search(
#         collection_name=COLLECTION_NAME_MarkaCollection,
#         query_vector=vector,
#         limit=total_points,
#         with_payload=True
#     )

#     # En yüksek skorlu sonucu al
#     best_match_marka = max(hits, key=lambda x: x.score, default=None)

#     if best_match_marka:
#         print("EN BENZER EŞLEŞME")
#         print(f"Benzer skor: {best_match_marka.score:.4f}")
#         print(f"Eşleşen ürün ID: {best_match_marka.id}")
#         print(f"Ek bilgiler: {best_match_marka.payload}")
#         print(f"Ürün adı (product_name): {best_match_marka.payload.get('product_name', 'Yok')}")
#         print("----------")
#         # if best_match_marka.payload.get('product_name') == Icim

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Kullanım: python qdrant_search.py path/to/image.jpg")
#     else:
#         image_path = sys.argv[1]
#         search_similar_image(image_path)


import sys
from qdrant_client import QdrantClient
from embedding_model import get_embedding

client = QdrantClient(host="localhost", port=6333)

def hierarchical_search(image_path):
    vector = get_embedding(image_path)

    def search(collection, vector):
        hits = client.search(
            collection_name=collection,
            query_vector=vector,
            limit=3,
            with_payload=True
        )
        return sorted(hits, key=lambda x: x.score, reverse=True)

    # 1. Marka seçimi
    marka_hits = search("MarkaCollection", vector)
    best_marka = max(marka_hits, key=lambda x: x.score, default=None)
    marka = best_marka.payload.get('product_name')  # "icim" veya "sutas"
    if marka == 'Icim':
        marka = 'icimSut'
    else:
        marka = 'sutasSut'

    # 2. Marka kategorisi (peynir/puding/sut)
    urun_hits = search(f"{marka}UrunleriCollection", vector)
    best_kategori = max(urun_hits, key=lambda x: x.score, default=None)
    kategori = best_kategori.payload.get('product_name')  # "peynir", "sut" veya "puding"

    if marka == 'icimSut':
        if kategori == 'Sut':
            kategori = 'icimSut'
        elif kategori == 'Peynir':
            kategori = 'icimPeynir'
        else:
            kategori = 'icimPuding'
    if marka == 'sutasSut':
        if kategori == 'Sut':
            kategori = 'sutasSut'
        elif kategori == 'Peynir':
            kategori = 'sutasPeynir'
        else:
            kategori = 'sutasPuding'

    # 3. Ürün tipi
    kategori_hits = search(f"{kategori}Collection", vector)
    best_urun = max(kategori_hits, key=lambda x: x.score, default=None)
    urun_adi = best_urun.payload.get("product_name")

    print(f"En uygun ürün: {urun_adi} ({best_urun.score:.4f})")

    print("\n--- Hiyerarşik Sonuçlar ---")
    print(f"Marka: {marka}")
    print(f"Kategori: {kategori}")
    print(f"Ürün: {urun_adi}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python qdrant_search.py path/to/image.jpg")
    else:
        hierarchical_search(sys.argv[1])