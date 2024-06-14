from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker, scoped_session

db = SQLAlchemy()
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# Initialize SQLAlchemy session management
SessionFactory = sessionmaker(bind=db.engine)
Session = scoped_session(SessionFactory)