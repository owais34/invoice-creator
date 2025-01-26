from flask import current_app, url_for

from database.models import Firm

def companyLogo(firm: Firm):
    with current_app.app_context():
        return url_for("firm.get_logo", firm_id= firm.id)

def companyName(firm: Firm):
    return firm.name

def companyDescription(firm: Firm):
    return firm.short_description

def companyAddress(firm: Firm):
    return f"{firm.address_line1} {firm.address_line2} {firm.address_line3}"

def companyPhone(firm: Firm):
    return firm.phone_number

def companyEmail(firm: Firm):
    return firm.email

def gstin(firm: Firm):
    return firm.gstin_number

def accountName(firm: Firm):
    return firm.account_name

def accountNumber(firm: Firm):
    return firm.account_number

def ifscCode(firm: Firm):
    return firm.ifsc_code

def bankName(firm: Firm):
    return firm.bank_name

def branchName(firm: Firm):
    return firm.branch_name

def thankMessage(firm: Firm):
    return firm.thank_message

def companySignature(firm: Firm):
    return f"For {firm.name}"


def get_value(field_name: str, company_id: str):
    firm: Firm = Firm.query.get(company_id)
    return globals()[field_name](firm)