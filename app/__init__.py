from flask import Flask
from app.controllers.job_controller import job_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(job_blueprint)
    return app
