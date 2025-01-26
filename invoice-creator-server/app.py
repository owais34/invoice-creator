from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate

from blueprints.firm import firm_blueprint
from database.setup import db

from blueprints.root_blueprint import root_blueprint
from settings import PORT, IS_DEV_ENVIRONMENT, DATABASE_URI

app = Flask(__name__)
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

app.register_blueprint(root_blueprint, url_prefix="/api/v1")
app.register_blueprint(firm_blueprint, url_prefix="/api/v1/firm")

if __name__ == "__main__":
    app.run()
