from paddleocr import PaddleOCR
import os

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def perform_ocr(image_path):
    result = ocr.ocr(image_path, cls=True)
    if not result or not result[0]:
        print("->",result)
        return [], image_path  # OCR sonucu boşsa, boş bir liste döndür
    txts = [elements[1][0] for elements in result[0]]
    return txts, image_path

def filter_texts(texts, image_path):
    filtered_texts = {}
    for text in texts:
        try:
            int(text)
        except ValueError:
            try:
                float(text)
            except ValueError:
                if image_path not in filtered_texts:
                    filtered_texts[image_path] = []
                filtered_texts[image_path].append(text)
    return filtered_texts

def get_img_paths():
    image_folder_path = "api/controller/execute_pdf/images/"
    images_name = os.listdir(image_folder_path)
    img_full_path = [os.path.join(image_folder_path, i) for i in images_name]
    return img_full_path

def process_image(image_path):
    try:
        texts, image_path = perform_ocr(image_path)
        if not texts:
            print(f"Resimde yazı tespit edilemedi: {image_path}")
            return None
        filtered_texts = filter_texts(texts, image_path)
        return filtered_texts
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

def all_filtered_texts():
    image_paths = get_img_paths()
    all_filtered_texts = {}
    for image_path in image_paths:
        result = process_image(image_path)
        if result:
            all_filtered_texts.update(result)
    return all_filtered_texts


