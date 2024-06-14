from . import db

class Pdf_docs(db.Model):
    __tablename__ = "PdfDoc"
    id = db.Column(db.Integer, primary_key=True)
    pdf_name = db.Column(db.String, unique=True, nullable=False)
    images = db.relationship("Image", back_populates="pdf_doc")
    tables = db.relationship("Table", back_populates="pdf_doc")
    texts = db.relationship("Text", back_populates="pdf_doc")
    address = db.relationship("Address", back_populates="pdf_doc")
    figureCaptions = db.relationship("FigureCaption", back_populates="pdf_doc")
    footers = db.relationship("Footer", back_populates="pdf_doc")
    formulas = db.relationship("Formula", back_populates="pdf_doc")
    headers = db.relationship("Header", back_populates="pdf_doc")
    listItems = db.relationship("ListItem", back_populates="pdf_doc")
    narrativeTexts = db.relationship("NarrativeText", back_populates="pdf_doc")
    pageBreaks = db.relationship("PageBreak", back_populates="pdf_doc")
    titles = db.relationship("Title", back_populates="pdf_doc")
    uncategorizedTexts = db.relationship("UncategorizedText", back_populates="pdf_doc")