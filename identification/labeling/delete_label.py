import os
import glob
import cv2
import sys
import numpy as np

labeled_folder = '/Users/mertalidincer/Documents/ZeroOneTouchProje1/opencv_face_labeling/val/labels/batch_13'
image_folder = '/Users/mertalidincer/Documents/ZeroOneTouchProje1/opencv_face_labeling/val/images/batch_13'

count = 0
rectangles = []
image = None
current_image_path = ""

colors = {
    0: (0, 0, 255),  # Kırmızı - head
    1: (0, 255, 0),  # Yeşil - body
    2: (255, 0, 0),  # Mavi - v_body
    3: (0, 255, 255)  # Sarı - face
}



def convert_to_normal_format(x_center, y_center, width, height, img_width, img_height):
    x1 = int((x_center - width / 2) * img_width)
    y1 = int((y_center - height / 2) * img_height)
    x2 = int((x_center + width / 2) * img_width)
    y2 = int((y_center + height / 2) * img_height)
    return x1, y1, x2, y2

def find_nearest_bbox(x, y, bboxes):
    min_distance = float('inf')
    nearest_bbox = None
    for bbox in bboxes:
        x1, y1, x2, y2 = bbox[1:]
        center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2
        distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_bbox = bbox
    return nearest_bbox

def draw_bounding_boxes(txt_file, image):
    global rectangles
    rectangles = []
    img_height, img_width = image.shape[:2]
    
    try:
        with open(txt_file, 'r') as f:
            for line in f:
                label_data = list(map(float, line.split()))
                if len(label_data) != 5:
                    continue
                label, x_center, y_center, width, height = label_data
                bbox = convert_to_normal_format(x_center, y_center, width, height, img_width, img_height)
                rectangles.append((label, *bbox))
                
                if label in [2, 3]:
                    continue
                
                color = colors.get(int(label), (255, 255, 255))
                cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
    except FileNotFoundError:
        print(f"Label file not found: {txt_file}")

def remove_bbox(x, y):
    global rectangles, current_image_path
    txt_file = os.path.join(labeled_folder, os.path.basename(current_image_path).rsplit('.', 1)[0] + '.txt')
    
    nearest_bbox = find_nearest_bbox(x, y, rectangles)
    if not nearest_bbox:
        print("No label found near the clicked point")
        return
    
    rectangles = [rect for rect in rectangles if rect != nearest_bbox]
    
    with open(txt_file, 'w') as f:
        for label, x1, y1, x2, y2 in rectangles:
            img_height, img_width = image.shape[:2]
            x_center = ((x1 + x2) / 2) / img_width
            y_center = ((y1 + y2) / 2) / img_height
            width = (x2 - x1) / img_width
            height = (y2 - y1) / img_height
            f.write(f"{int(label)} {x_center} {y_center} {width} {height}\n")
    
    update_image()

def update_image():
    global image, current_image_path
    image = cv2.imread(current_image_path)
    image = cv2.resize(image, (3000, 1700))
    txt_file = os.path.join(labeled_folder, os.path.basename(current_image_path).rsplit('.', 1)[0] + '.txt')
    draw_bounding_boxes(txt_file, image)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left click: x={x}, y={y}")
        remove_bbox(x, y)

def process_single_image(image_path):
    global image, current_image_path, count
    current_image_path = image_path
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image file not found: {image_path}")
        return
    
    image = cv2.resize(image, (3000, 1700))
    
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Image", click_event)
    
    labeled_image(image_path, image)
    
    while True:
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('h'):
            count += 1
            print(count)
            break
        elif key == ord('q'):
            cv2.destroyAllWindows()
            sys.exit()
    
    cv2.destroyAllWindows()

def labeled_image(image_path, image):
    txt_file = os.path.join(labeled_folder, os.path.basename(image_path).rsplit('.', 1)[0] + '.txt')
    draw_bounding_boxes(txt_file, image)

def process_images_in_folder(folder_path):
    image_files = []
    extensions = ["*.jpg", "*.jpeg", "*.png"]
    
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(folder_path, ext)))
    
    if not image_files:
        print("Image not found in folder")
        return
    
    for img_path in image_files:
        process_single_image(img_path)

if __name__ == "__main__":
    process_images_in_folder(image_folder)
