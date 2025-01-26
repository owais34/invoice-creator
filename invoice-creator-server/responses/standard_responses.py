from flask import jsonify


def success_response(message: str = "ok", data = None):
    response = {
        "status": "success",
        "message": message
    }

    if data is not None:
        response["data"] = data

    return jsonify(response)

def failure_response(message: str, data = None):
    response = {
        "status": "failure",
        "message": message
    }
    if data is not None:
        response["data"] = data

    return jsonify(response)

def error_response(message: str = "Error encountered", error: Exception = None):
    response = {
        "status": "error",
        "message": message,
        "error": str(error)
    }
    return jsonify(response)