import os
import shutil
import sys
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from flask_migrate import Migrate

from blueprints.firm import firm_blueprint
from database.setup import db

from blueprints.root_blueprint import root_blueprint
from settings import PORT, IS_DEV_ENVIRONMENT, DATABASE_URI, db_path


app = Flask(__name__, static_folder='client', static_url_path='')

cors = CORS(app)
config = {
    "DEBUG": IS_DEV_ENVIRONMENT,
    "PORT": PORT,
    "CORS_HEADERS": "Content-Type",
    "SQLALCHEMY_DATABASE_URI": DATABASE_URI
}

app.config.from_mapping(config)
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)


@app.route('/')
def index():
    return send_from_directory(os.path.join(app.static_folder), "index.html")

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder), path)


app.register_blueprint(root_blueprint, url_prefix="/api/v1")
app.register_blueprint(firm_blueprint, url_prefix="/api/v1/firm")

def create_db():
    if not os.path.exists(db_path):  # Check if the SQLite database file exists
        print("Database not found. Creating the database...")
        db.create_all()  # This will create the tables defined in the models
        print("Database created successfully.")
    else:
        print("Database already exists.")

if __name__ == "__main__":
    create_db()
    app.run()
