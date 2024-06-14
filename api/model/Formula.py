from . import db, Pdf_docs


class Formula(db.Model):
    __tablename__ = "Formula"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=True)
    meta_data = db.Column(db.JSON, nullable=True)
    pdf_document_id = db.Column(db.Integer, db.ForeignKey(Pdf_docs.id),nullable=False)
    pdf_doc = db.relationship("Pdf_docs", back_populates="formulas")