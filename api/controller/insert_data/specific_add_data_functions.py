from sqlalchemy.exc import SQLAlchemyError
from api.model import *

def add_pdf_document(session, filename):
    try:
        pdf_doc = session.query(Pdf_docs).filter_by(pdf_name=filename).first()
        if not pdf_doc:
            pdf_doc = Pdf_docs(pdf_name=filename)
            session.add(pdf_doc)
            session.commit()
        print(f"Added Pdf_doc: {pdf_doc.id}")
        return pdf_doc
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding PDF document: {e}")
        return None

def add_data_to_pdf(session, model_class, pdf_document, content=None, metadata=None,img_text=None):
    try:
        new_record = model_class(
            content=content,
            meta_data=metadata,
            pdf_document_id=pdf_document.id
        )
        if model_class==Image:
            new_record = model_class(
                content=content,
                meta_data=metadata,
                img_text=img_text,
                pdf_document_id=pdf_document.id
            )
        session.add(new_record)
        session.commit()
        print(f"Added {model_class.__name__}: {new_record.id}")
        return new_record
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding {model_class.__name__}: {e}")
        return None


def add_image_to_pdf(session, pdf_document, content=None, metadata=None,img_text=None):
    return add_data_to_pdf(session, Image, pdf_document, content, metadata,img_text)


def add_narrative_text_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, NarrativeText, pdf_document, content, metadata)


def add_address_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Address, pdf_document, content, metadata)


def add_figure_caption_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, FigureCaption, pdf_document, content, metadata)


def add_footer_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Footer, pdf_document, content, metadata)


def add_formula_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Formula, pdf_document, content, metadata)


def add_header_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Header, pdf_document, content, metadata)


def add_listItem_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, ListItem, pdf_document, content, metadata)


def add_pageBreak_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, PageBreak, pdf_document, content, metadata)


def add_table_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Table, pdf_document, content, metadata)


def add_text_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Text, pdf_document, content, metadata)


def add_uncategorizedText_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, UncategorizedText, pdf_document, content, metadata)


def add_title_to_pdf(session, pdf_document, content=None, metadata=None):
    return add_data_to_pdf(session, Title, pdf_document, content, metadata)
