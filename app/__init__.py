from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(): # The function we made in run.py
    app = Flask(__name__, instance_relative_config=False) 
    app.config.from_object("config.Config")

    with app.app_context():
        db.init_app(app)        
        import .routes
        
        return app