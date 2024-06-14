from flask import Blueprint, render_template, request
from api.model.Images import Image
from api.model.Tables import Table
from api.model.Texts import Text
from api.model.Address import Address
from api.model.FigureCaption import FigureCaption
from api.model.Footer import Footer
from api.model.Formula import Formula
from api.model.Header import Header
from api.model.ListItem import ListItem
from api.model.NarrativeText import NarrativeText
from api.model.PageBreak import PageBreak
from api.model.Title import Title
from api.model.UncategorizedText import UncategorizedText

view_bp = Blueprint('view_bp', __name__,template_folder="api/view/templates")

model_mapping = {
    'Images': Image,
    'Tables': Table,
    'Texts': Text,
    'Addresses': Address,
    'FigureCaptions': FigureCaption,
    'Footers': Footer,
    'Formulas': Formula,
    'Headers': Header,
    'ListItems': ListItem,
    'NarrativeTexts': NarrativeText,
    'PageBreaks': PageBreak,
    'Titles': Title,
    'UncategorizedTexts': UncategorizedText
}


@view_bp.route('/view_data', methods=['POST','GET'])
def view_data():
    table_name = request.form.get('table_name')
    model = model_mapping.get(table_name)
    if not model:
        return render_template('viewData.html', error="Invalid table name")

    data = model.query.all()
    result = []
    for item in data:
        item_data = {col.name: getattr(item, col.name) for col in item.__table__.columns}
        result.append(item_data)
    return render_template('viewData.html', data=result)

