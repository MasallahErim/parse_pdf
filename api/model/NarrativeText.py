from . import db, Pdf_docs


class NarrativeText(db.Model):
    __tablename__ = "NarrativeText"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)
    pdf_document_id = db.Column(db.Integer, db.ForeignKey(Pdf_docs.id),nullable=False)
    pdf_doc = db.relationship("Pdf_docs", back_populates="narrativeTexts")