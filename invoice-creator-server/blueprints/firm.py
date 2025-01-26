import os.path
import traceback

from flask import Blueprint, jsonify, request, abort, send_from_directory, send_file
import uuid

from database.models import Firm
from database.setup import db
from responses.standard_responses import success_response, failure_response, error_response
from settings import UPLOAD_FOLDER_PATH
from templates.invoice import default_template
from templates.invoice_value_getters import get_value

firm_blueprint = Blueprint("firm", __name__)
allowed_files = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename: str):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_files

@firm_blueprint.get("/")
def get_all():
    firms = Firm.query.all()
    firm_names = []
    for firm in firms:
        firm_names.append({
            "name": firm.name,
            "id": firm.id
        })

    return success_response(data=firm_names), 200

@firm_blueprint.post("/")
def add():
    request_data = request.form
    print(request_data)
    logo_image_file = None
    logo_image_file_name = None
    if "logo_image" in request.files:
        logo_image_file = request.files["logo_image"]
    if logo_image_file and allowed_file(logo_image_file.filename):
        ext = logo_image_file.filename.rsplit('.', 1)[1].lower()
        logo_image_file_name = f"{uuid.uuid4()}.{ext}"
        logo_image_file.save(os.path.join(UPLOAD_FOLDER_PATH, logo_image_file_name))
        print("File saved")

    try:
        firm = Firm()
        firm.name = request_data.get("companyName")
        firm.email = request_data.get("companyEmail")
        firm.short_description = request_data.get("companyDescription")
        firm.phone_number = request_data.get("companyPhone")
        firm.address_line1 = request_data.get("companyAddress")
        firm.address_line2 = ""
        firm.address_line3 = ""
        firm.gstin_number = request_data.get("gstin")
        firm.account_name = request_data.get("accountName")
        firm.account_number = request_data.get("accountNumber")
        firm.ifsc_code = request_data.get("ifscCode")
        firm.bank_name = request_data.get("bankName")
        firm.branch_name = request_data.get("branchName")
        firm.thank_message = request_data.get("thankMessage")
        if logo_image_file_name:
            firm.logo_image_path = logo_image_file_name
        db.session.add(firm)
        db.session.commit()
        return success_response("Created") , 201
    except Exception as e:
        db.session.rollback()
        traceback.print_exc()
        return error_response(error=e), 400

@firm_blueprint.get("/<firm_id>/logo")
def get_logo(firm_id):
    try:
        firm: Firm = Firm.query.get(firm_id)
        image_path = str(os.path.join(UPLOAD_FOLDER_PATH, firm.logo_image_path))
        if not os.path.isfile(image_path):
            abort(404)  # If the image does not exist, return a 404 error
            # Serve the image
        return send_file(image_path)
    except Exception as e:
        traceback.print_exc()
        return abort(404)

@firm_blueprint.get("/form")
def get_add_firm_form():
    try:
        form_fields = []
        for section in default_template:
            for field_spec in default_template.get(section):
                if field_spec["type"] == "autofill":
                    form_fields.append(field_spec)
        return success_response(data=form_fields)
    except Exception as e:
        traceback.print_exc()
        return abort(404)

@firm_blueprint.get("/<firm_id>/invoiceForm")
def get_firm_invoice_form(firm_id):
    try:
        firm: Firm = Firm.query.get(firm_id)
        invoice_template = firm.get_invoice_template()
        for section in invoice_template:
            for field_spec in invoice_template[section]:
                if field_spec["type"] == "autofill":
                    field_value = get_value(field_spec["field"], firm_id)
                    if "formAttributes" not in field_spec:
                        field_spec["formAttributes"] = {"type": "text"}
                    field_spec["formAttributes"]["value"] = field_value
                pass
        return success_response(data=invoice_template)
    except Exception as e:
        traceback.print_exc()
        return abort(404)









