"""
    ResNet50
"""
# import torch
# from torchvision import models, transforms
# from PIL import Image

# # CPU kullanımı
# device = torch.device("cpu")

# # ResNet50 modelini yükle
# model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
# embedding_model = torch.nn.Sequential(*list(model.children())[:-1])
# embedding_model = embedding_model.to(device)
# embedding_model.eval()

# # Görsel dönüşüm tanımı
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406],
#                          std=[0.229, 0.224, 0.225])
# ])

# # Görselden embedding çıkarma fonksiyonu
# def get_embedding(image_path):
#     image = Image.open(image_path).convert("RGB")
#     tensor = transform(image).unsqueeze(0).to(device)
#     with torch.no_grad():
#         embedding = embedding_model(tensor)
#     embedding = embedding.view(-1)
#     return embedding.cpu().numpy().astype("float32")


"""   
    CLIP
"""
# import torch
# import clip
# from PIL import Image

# # Cihaz seçimi
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # CLIP modelini yükle
# model, preprocess = clip.load("ViT-B/32", device=device)

# # Görselden embedding çıkarma fonksiyonu
# def get_embedding(image_path):
#     image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
#     with torch.no_grad():
#         image_features = model.encode_image(image)
#     image_features = image_features / image_features.norm(dim=-1, keepdim=True)  # normalize
#     return image_features.squeeze(0).cpu().numpy().astype("float32")

"""
    openai/clip-vit-base-patch32
"""
    ######## Soon
"""
    fashion-clip
"""

import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# Cihaz ayarı
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# FashionCLIP modelini ve işlemcisini yükle
model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip").to(device)
processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

def get_embedding(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.get_image_features(**inputs)
    embedding = outputs.squeeze().cpu().numpy().astype("float32")
    return embedding


"""
    openai/clip-vit-base-patch32
"""
# import torch
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModelm
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # Model ve işlemciyi yükle
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
# processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
# from transformers import AutoModel, AutoProcessor
# model = AutoModel.from_pretrained('Marqo/marqo-fashionCLIP', trust_remote_code=True)
# processor = AutoProcessor.from_pretrained('Marqo/marqo-fashionCLIP', trust_remote_code=True)**

# # Görselden embedding çıkaran fonksiyon
# def get_embedding(image_path):
#     image = Image.open(image_path).convert("RGB")
#     inputs = processor(images=image, return_tensors="pt").to(device)
#     with torch.no_grad():
#         features = model.get_image_features(**inputs)
#     return features.squeeze().cpu().numpy().astype("float32")

# # Cosine similarity hesapla
# def similarity(img1_path, img2_path):
#     emb1 = get_embedding(img1_path).reshape(1, -1)
#     emb2 = get_embedding(img2_path).reshape(1, -1)
#     score = cosine_similarity(emb1, emb2)[0][0]
#     return score

# # Örnek kullanım
# if __name__ == "__main__":
#     img1 = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Gıda/icim/Peynir/BeyazPeynir/icim-tam-yagli-beyaz-peynir-900-g.jpg"
#     img2 = "/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Gıda/Sütaş/Peynir/BeyazPeynir/Beyaz-Peynir-700-gr.jpg"
#     sim_score = similarity(img1, img2)
#     print(f"Benzerlik skoru: {sim_score:.4f}")

""" 
    hiyerarsik mebeding
"""

# import torch
# from PIL import Image
# from transformers import CLIPProcessor, CLIPModel

# # Cihaz ayarı
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # FashionCLIP modelini ve işlemcisini yükle
# model = CLIPModel.from_pretrained("patrickjohncyh/fashion-clip").to(device)
# processor = CLIPProcessor.from_pretrained("patrickjohncyh/fashion-clip")

# def create_hierarchical_text(category_list, product_name):
#     """
#     Kategori listesini ve ürün adını birleştirerek hiyerarşik metin oluşturur.
#     """
#     return " > ".join(category_list) + " : " + product_name

# def get_hierarchical_embedding(image_path, category_list, product_name):
#     """
#     Görsel ve hiyerarşik metinden birleşik embedding çıkarır.
#     """
#     image = Image.open(image_path).convert("RGB")
#     text = create_hierarchical_text(category_list, product_name)

#     inputs = processor(
#         text=[text],
#         images=[image],
#         return_tensors="pt",
#         padding=True,
#         truncation=True
#     ).to(device)

#     with torch.no_grad():
#         outputs = model(**inputs)

#     image_emb = outputs.image_embeds[0]
#     text_emb = outputs.text_embeds[0]

#     combined = (image_emb + text_emb) / 2  # Ortalaması alınabilir
#     return combined.cpu().numpy().astype("float32")

import numpy as np

def calculate_mean_vector(vec1, vec2, vec3):
    """
    İki vektörün ortalamasını hesaplar ve döndürür.

    Args:
        vec1 (numpy.ndarray): Birinci vektör.
        vec2 (numpy.ndarray): İkinci vektör.

    Returns:
        numpy.ndarray: İki vektörün ortalaması.
    """
    # Vektörleri birleştir
    vectors = np.array([vec1, vec2, vec3])
    
    # Ortalamayı hesapla
    mean_vector = np.mean(vectors, axis=0)
    
    return mean_vector

"""
    ocr microsoft
"""

# from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# from PIL import Image
# import torch

# # Model ve işlemci
# processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-stage1")
# model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-stage1")
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# # Görseli yükle
# image = Image.open("/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Screenshot.png").convert("RGB")

# # OCR işlemi
# pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)
# generated_ids = model.generate(pixel_values)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

# print("Okunan metin:", generated_text)

"""
    ocr paddleocr
"""

# from paddleocr import PaddleOCR

# ocr = PaddleOCR(use_angle_cls=True, lang='en') 
# result = ocr.ocr('/Users/mertalidincer/Documents/zot_staj/inventory_management_system/image_embedding/train/Screenshot.png', cls=True)

# for line in result[0]:
#     print(line[1][0])  # sadece metni yazdır


# from torchvision import datasets, transforms
# from torch.utils.data import DataLoader

# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
# ])

# train_dataset = datasets.ImageFolder(root="/Users/mertalidincer/Documents/zot_staj/RP2K_dataset/train", transform=transform)
# train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# from transformers import CLIPModel

# model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
# vision_encoder = model.vision_model

# import torch.nn as nn

# class CLIPFineTuner(nn.Module):
#     def __init__(self, clip_model, num_classes):
#         super().__init__()
#         self.vision_encoder = clip_model.vision_model
#         self.classifier = nn.Linear(clip_model.config.projection_dim, num_classes)

#     def forward(self, pixel_values):
#         outputs = self.vision_encoder(pixel_values=pixel_values)
#         pooled_output = outputs.pooler_output  # shape: (batch_size, 768)
#         return self.classifier(pooled_output)

# import torch

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# num_classes = len(train_dataset.classes)

# model = CLIPFineTuner(model, num_classes).to(device)
# optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
# criterion = nn.CrossEntropyLoss()

# for epoch in range(10):
#     model.train()
#     for images, labels in train_loader:
#         images, labels = images.to(device), labels.to(device)

#         optimizer.zero_grad()
#         outputs = model(images)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

#     print(f"Epoch {epoch+1} Loss: {loss.item():.4f}")

# import os
# import pandas as pd

# root_dir = "/Users/mertalidincer/Documents/zot_staj/RP2K_dataset/train"  
# rows = []

# for product_dir in os.listdir(root_dir):
#     product_path = os.path.join(root_dir, product_dir)
#     if os.path.isdir(product_path):
#         caption = product_dir.replace("_", " ")
#         for img_file in os.listdir(product_path):
#             if img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
#                 img_path = os.path.join(product_path, img_file)
#                 rows.append([img_path, caption])

# df = pd.DataFrame(rows, columns=["image", "text"])
# df.to_csv("rp2k_train_metadata.csv", index=False)


"""
    klasor ve dosyalari yeniden isimlendirme
"""

# import os

# root_test = "/Users/mertalidincer/Documents/zot_staj/RP2K_dataset/test"

# folders = sorted([f for f in os.listdir(root_test) if os.path.isdir(os.path.join(root_test, f))])

# for i, folder in enumerate(folders, 1):
#     old_path = os.path.join(root_test, folder)
#     new_path = os.path.join(root_test, str(i))
#     os.rename(old_path, new_path)
#     print(f"{folder} -> {i}")

