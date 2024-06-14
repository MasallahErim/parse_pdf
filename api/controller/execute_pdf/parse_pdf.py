from PIL import Image as PILImage
import numpy as np
import os
from ..execute_pdf.singleton import PdfExtractorSingleton


def extract_data_from_pdf(pdf_file_path, image_output_directory):
    pdf_extractor = PdfExtractorSingleton(
        pdf_file_path=pdf_file_path,
        image_output_directory=image_output_directory)
    elements = pdf_extractor.get_elements()
    return elements


def categorize_extracted_elements(elements):
    categories = ["FigureCaption", "NarrativeText", "ListItem", "Title",
                  "Address", "Table", "PageBreak", "Header", "Footer",
                  "UncategorizedText", "Image", "Formula", "PageNumber"]
    extracted_data = {
        "FigureCaption": [], "NarrativeText": [], "ListItem": [],
        "Title": [], "Address": [], "Table": [], "PageBreak": [],
        "Header": [], "Footer": [], "UncategorizedText": [],
        "Image": [], "Formula": [], "PageNumber": []}
    for element in elements:
        for category in categories:
            if element.category == category:
                if category == "Table":
                    extracted_data[category].append([element.metadata.text_as_html, element.metadata.to_dict(),
                                                     element])
                elif category == "Image":
                    extracted_data[category].append([[], element.metadata.to_dict(), element])
                else:
                    extracted_data[category].append([element.text, element.metadata.to_dict(), element])
    return extracted_data


def process_extracted_images(image_output_directory):
    image_data = []
    for image_filename in os.listdir(image_output_directory):
        image_path = os.path.join(image_output_directory, image_filename)
        loaded_image = PILImage.open(image_path)
        image_array = np.array(loaded_image)
        image_data.append(image_array)
    return image_data


def execute_extraction(pdf_file_path, image_output_directory):
    elements = extract_data_from_pdf(pdf_file_path, image_output_directory)
    extracted_data = categorize_extracted_elements(elements)
    process_extracted_images(image_output_directory)
    return extracted_data
