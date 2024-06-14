from flask import Flask
from api.controller.process.parse_pdf import parse_pdf
from api.view.query_view_data.view import  view_bp
from api.model import *
from api.controller.process.save_upload_pdf import upload_pdf_bp
UPLOAD_FOLDER = 'api/controller/process/saved_pdf'
def create_app():
    app = Flask(__name__, template_folder="api/view/templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@db:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 't8'
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("Tables created successfully")
    app.register_blueprint(upload_pdf_bp)
    app.register_blueprint(parse_pdf)
    app.register_blueprint(view_bp)
    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8888, host="0.0.0.0")








