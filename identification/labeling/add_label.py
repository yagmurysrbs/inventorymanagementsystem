import os 
from PIL import Image
import glob
import cv2
import sys
import uuid
colors = {
    0: (0, 0, 255),  # Kırmızı - head
    1: (0, 255, 0),  # Yeşil - body
    2: (255, 0, 0),  # Mavi - v_body
    3: (0, 255, 255)  # Sarı - face
}

drawing = False
ix, iy = -1, -1
rectangles = []
image:cv2.Mat = None
current_label = 0
labeled_folder = '/Users/mertalidincer/Documents/zot_staj/opencv_face_labeling/labels1000'
image_path = '/Users/mertalidincer/Documents/zot_staj/opencv_face_labeling/images1000'
delete_rectangles = []
dots = []
count = 0

def get_id():
    unique_id = str(uuid.uuid4())  # Örneğin: 123e4567-e89b-12d3-a456-426614174000
    return unique_id

def process_image_in_folder(folder_path):
    """Klasördeki tüm görselleri işler."""
    image_files = []
    extensions = ["*.jpg", "*.jpeg", "*.png"]

    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))

    if not image_files:
        print("Klasörde işlenecek resim bulunamadı!")
        return

    for image_path in image_files:
        process_single_image(image_path)
    

def process_single_image(image_path):
    """Tek bir resmi işler, etiketlerini yükler ve ekranda gösterir."""
    global image, count

    os.makedirs(labeled_folder, exist_ok=True)

    txt_file = os.path.join(labeled_folder, os.path.basename(image_path).rsplit('.', 1)[0] + '.txt')

    # Eğer ilgili .txt dosyası yoksa oluştur
    if not os.path.exists(txt_file): 
        open(txt_file, 'w').close()  

    image = cv2.imread(image_path)
    if image is None: 
        print(f"Resim dosyası yüklenemedi: {image_path}")
        return
    count += 1
    print(count)
    image = cv2.resize(image, (3840, 2160))  # Görüntüyü ekrana uygun boyutlandır
    labeled_image(image_path, image)
    
    cv2.namedWindow('Resim')
    cv2.setMouseCallback("Resim", draw_recrangle)
    cv2.imshow('Resim', image)

    try: 
        while True:
            print(image_path)
            key = cv2.waitKey(0) & 0XFF            
            if key in [ord('0'), ord('1'), ord('2'), ord('3')]:  # Etiket kodu seçimi
                current_label = int(chr(key))
                print(f"Etiket kodu değiştirildi: {current_label}")
            elif key == 13: 
                if rectangles:
                    ix1, iy1, ix2, iy2, _= rectangles[-1]
                    rectangles[-1] = (ix1, iy1, ix2, iy2, current_label)
                    color = colors[current_label]
                    cv2.rectangle(image, (ix1, iy2), (ix2, iy2), color, 2)
                    cv2.imshow('Resim', image)
                    x_center, y_center, width, height = convert_to_yolo_format(ix1, iy1, ix2, iy2)
                    with open(txt_file, 'a') as f:
                        f.write(f"{current_label} {x_center} {y_center} {width} {height} \n")
            
            elif key == ord('z'): 
                if rectangles:
                    rectangles.pop()
                    image = cv2.imread(image_path)
                    # etiketi dosyadan sil
                    with open(txt_file, 'r') as f:
                        lines = f.readlines()
                    with open(txt_file, 'w') as f:
                        for i, line in enumerate(lines):
                            if i != len(lines) - 1: 
                                f.write(line)
                    # Resmi yeniden boyutlandir
                    image = cv2.resize(image, (3500, 2000))
                    # Etiket dosyasındaki koordinatları yeniden oku ve dikdörtgenleri çiz
                    draw_bounding_boxes(txt_file, image)
                    cv2.imshow('Resim', image)

            #elif key == ord('p'):

            elif key == ord('r'):
                break
            elif key == ord('q'):
                cv2.destroyAllWindows()
                sys.exit()


    except KeyboardInterrupt:
        print("program durduruldu")
    finally:
        cv2.destroyAllWindows()

"""Fare ile dikdörtgen çizme fonksiyonu."""
def draw_recrangle(event, x, y, flags, param):
    global ix, iy, drawing, image, rectangles, dots

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_image = image.copy()
            cv2.rectangle(temp_image, (ix, iy), (x, y), (255, 255, 255), 1)
            cv2.imshow("Resim", temp_image)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rectangles.append((ix, iy, x, y, current_label))
        cv2.rectangle(image, (ix, iy), (x, y), colors[current_label])
        

def labeled_image(image_path, image):
    """Etiketleri yükleyip çizim yapar ve ekranda gösterir."""
    txt_file = os.path.join(labeled_folder, os.path.basename(image_path).rsplit('.', 1)[0] + '.txt')

    try:
        draw_bounding_boxes(txt_file, image)
    except FileNotFoundError:
        print(f"Etiket dosyası bulunamadı: {txt_file}")

"""Etiket dosyasındaki koordinatları okuyup resme çizer."""
def draw_bounding_boxes(txt_file, image:cv2.Mat):
    print(f"İşlenen etiket dosyası: {txt_file}")

    img_height, img_width = image.shape[:2]

    with open(txt_file, 'r') as f:
        for line in f:
            label_data = list(map(float, line.split()))
            if len(label_data) != 5:
                continue # eksik veri var gec

            label, x_center, y_center, width,height = label_data
            if label in [2, 3]:
                continue
            x1, y1, x2, y2 = convert_to_normal_format(x_center, y_center, width, height)
            color = colors.get(int(label), (255, 255, 255))  # Geçersiz label durumunda beyaz çiz
            
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, f"Class {int(label)}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)       
 
def convert_to_normal_format(x_center, y_center, width, height):
    """YOLO formatındaki koordinatları piksel değerlerine çevirir."""
    img_height, img_width = image.shape[:2]

    x1 = int((x_center - width / 2) * img_width)
    y1 = int((y_center - height / 2) * img_height)
    x2 = int((x_center + width / 2) * img_width)
    y2 = int((y_center + height / 2) * img_height)

    return x1, y1, x2, y2

def check_limits(value):
    if value < 0:
        return 0
    elif value > 1:
        return 1
    else:
        return value
    
def convert_to_yolo_format(x1, y1, x2, y2):
    global image
    img_height, img_width = image.shape[:2]
    x_center = ((x1 + x2) /2) / img_width
    y_center = ((y1 + y2) /2) / img_height
    width = (x2 - x1) / img_width
    height = (y2 - y1) / img_height
    x_center = check_limits(x_center)
    y_center = check_limits(y_center)
    width = check_limits(width)
    height = check_limits(height)
    return x_center, y_center, width, height




# İşlem başlatılıyor
process_image_in_folder(image_path)
