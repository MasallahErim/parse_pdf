from flask import Blueprint, request, render_template, current_app,session
from werkzeug.utils import secure_filename
import os

upload_pdf_bp = Blueprint('upload_pdf_bp', __name__, template_folder='api/view/templates')

ALLOWED_EXTENSIONS = {'pdf'}
UPLOAD_FOLDER = 'api/controller/process/saved_pdf'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def is_pdf_already_uploaded(filename):

    existing_files = os.listdir(UPLOAD_FOLDER)
    return filename in existing_files


@upload_pdf_bp.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return render_template('upload.html', message="No file part")


        pdf_file = request.files['pdf_file']
        if pdf_file.filename == '':
            return render_template('upload.html', message="No selected file")

        if pdf_file and allowed_file(pdf_file.filename):
            filename = secure_filename(pdf_file.filename)

            if is_pdf_already_uploaded(filename):
                return render_template('upload.html', message="PDF has already been uploaded previously.",
                                       filename=filename)

            upload_folder = current_app.config['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            pdf_file.save(file_path)
            session['uploaded_pdf'] = filename
            return render_template('upload.html', message=f"PDF saved to {file_path} successfully", filename=filename)
        else:
            return render_template('upload.html', message="Invalid file format")
    return render_template('upload.html')


@upload_pdf_bp.route('/view_datas', methods=['GET'])
def view_data():
    return render_template('view_data.html')







