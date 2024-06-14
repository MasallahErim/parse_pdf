
from flask import Blueprint, render_template, session
from api.controller.insert_data.insert_data import process_pdf

parse_pdf = Blueprint('parse_pdf', __name__, template_folder='templates')

@parse_pdf.route('/process', methods=['POST'])
def process_pdf_endpoint():
	try:
    	
		filename = session.get('uploaded_pdf')
		session.clear()
		print(filename)
		process_pdf(filename)
		return render_template('upload.html', message="PDF processed successfully")
	except Exception as e:
		return render_template('upload.html', message=f"Error processing PDF: {str(e)}")
