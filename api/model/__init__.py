from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .PdfDocs import Pdf_docs
from .Texts import Text
from .Images import Image
from .Tables import Table
from .Address import Address
from .Formula import Formula
from .ListItem import ListItem
from .Title import Title
from .UncategorizedText import UncategorizedText
from .Texts import Text
from .Header import Header
from .Footer import Footer
from .PageBreak import PageBreak
from .FigureCaption import FigureCaption
from .NarrativeText import NarrativeText