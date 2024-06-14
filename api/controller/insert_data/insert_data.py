import os
from flask import current_app
from sqlalchemy.orm import sessionmaker
from ..execute_pdf.parse_pdf import execute_extraction
from ..insert_data.specific_add_data_functions import *
from ..OCR.img_to_text import all_filtered_texts
def add_data_to_database(session, datas, fileName: str):
    img_text = all_filtered_texts()
    pdf_doc = add_pdf_document(session, fileName)
    for item in datas:
        for data in datas[item]:
            content = data[0]
            meta_data = data[1]
            if item == 'Image':
                contents = data[1]["image_path"]
                metadatas = data[1]
                add_image_to_pdf(session, pdf_doc, contents, metadatas,img_text[contents])
            elif item == 'NarrativeText':
                add_narrative_text_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Address':
                add_address_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'FigureCaption':
                add_figure_caption_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Footer':
                add_footer_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Formula':
                add_formula_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Header':
                add_header_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'ListItem':
                add_listItem_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'PageBreak':
                add_pageBreak_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Title':
                add_title_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'UncategorizedText':
                add_uncategorizedText_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Table':
                add_table_to_pdf(session, pdf_doc, content, meta_data)
            elif item == 'Text':
                add_text_to_pdf(session, pdf_doc, content, meta_data)

def process_pdf(pdf_name):
    with current_app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        pdf_path = os.path.join(current_app.config['UPLOAD_FOLDER'], pdf_name)
        allData = execute_extraction(pdf_file_path=pdf_path,
                                     image_output_directory="api/controller/execute_pdf/images")
        add_data_to_database(session, allData,pdf_name)




