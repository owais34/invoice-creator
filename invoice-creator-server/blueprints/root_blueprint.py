from flask import Blueprint, jsonify

root_blueprint = Blueprint("root", __name__)

@root_blueprint.route("/", methods=["GET"])
def get_users():
    return jsonify({
        "message" : "Working"
    })