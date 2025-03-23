import json
from email.policy import default

from sqlalchemy.orm import mapped_column

from database.setup import db
from templates.invoice import json_format_default_template, json_format_custom_fields


class Firm(db.Model):
    id = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name = mapped_column(db.String(80), nullable=False)
    short_description = mapped_column(db.String(80), default="")
    phone_number = mapped_column(db.String(15), default="")
    address_line1 = mapped_column(db.String(35), default="")
    address_line2 = mapped_column(db.String(35), default="")
    address_line3 = mapped_column(db.String(35), default="")
    email = mapped_column(db.String(120), default="")
    gstin_number = mapped_column(db.String(35), default="")
    logo_image_path = mapped_column(db.String(1024), nullable=True)
    invoice_template = mapped_column(db.LargeBinary, nullable=False, default=json_format_default_template.encode())
    account_name = mapped_column(db.String(120), default="")
    account_number = mapped_column(db.String(100), default="")
    ifsc_code = mapped_column(db.String(100), default="")
    bank_name = mapped_column(db.String(100), default="")
    branch_name = mapped_column(db.String(100), default="")
    thank_message = mapped_column(db.String(100), default="")
    sgst = mapped_column(db.Numeric, default=0, nullable=False)
    igst = mapped_column(db.Numeric, default=0, nullable=False)
    cgst = mapped_column(db.Numeric, default=0, nullable=False)
    custom_fields = mapped_column(db.LargeBinary, nullable=False, default=json_format_custom_fields.encode())


    def get_invoice_template(self) -> dict:
        return json.loads(self.invoice_template.decode())

    def set_invoice_template(self, invoice_template: dict):
        self.invoice_template = json.dumps(invoice_template).encode()