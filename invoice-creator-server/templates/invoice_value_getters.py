import math

from flask import current_app, url_for

from database.models import Firm
from templates.utils import convert_to_words


def companyLogo(firm: Firm, **kwargs):
    with current_app.app_context():
        return url_for("firm.get_logo", firm_id= firm.id, _external=True)

def companyName(firm: Firm, **kwargs):
    return firm.name

def companyDescription(firm: Firm, **kwargs):
    return firm.short_description

def companyAddress(firm: Firm, **kwargs):
    return f"{firm.address_line1} {firm.address_line2} {firm.address_line3}"

def companyPhone(firm: Firm, **kwargs):
    return firm.phone_number

def companyEmail(firm: Firm, **kwargs):
    return firm.email

def gstin(firm: Firm, **kwargs):
    return firm.gstin_number

def accountName(firm: Firm, **kwargs):
    return firm.account_name

def accountNumber(firm: Firm, **kwargs):
    return firm.account_number

def ifscCode(firm: Firm, **kwargs):
    return firm.ifsc_code

def bankName(firm: Firm, **kwargs):
    return firm.bank_name

def branchName(firm: Firm, **kwargs):
    return firm.branch_name

def thankMessage(firm: Firm, **kwargs):
    return firm.thank_message

def companySignature(firm: Firm, **kwargs):
    return f"For {firm.name}"

def sgst(firm: Firm, **kwargs) -> float:
    return float(firm.sgst)

def igst(firm: Firm, **kwargs) -> float:
    return float(firm.igst)

def cgst(firm: Firm, **kwargs) -> float:
    return float(firm.cgst)

def amount(firm: Firm, **kwargs) -> float:
    if not kwargs.get("amount"):
        rows: list[dict] = kwargs.get("Table Details")
        total = 0
        for row in rows:
            total += float(row["amount"])
        kwargs["amount"] = total
    return kwargs.get("amount")

def totalAmount(firm: Firm, **kwargs) -> float:
    if not kwargs.get("totalAmount"):
        totalAmt = amount(firm, **kwargs)
        totalAmt += cgstAmount(firm, **kwargs)
        totalAmt += sgstAmount(firm, **kwargs)
        totalAmt += roundOff(firm, **kwargs)
        kwargs["totalAmount"] = round(totalAmt, 2)
    return kwargs.get("totalAmount")

def sgstAmount(firm: Firm, **kwargs) -> float:
    if not kwargs.get("sgstAmount"):
        total = amount(firm, **kwargs)
        value = (sgst(firm) * total)/100
        kwargs["sgstAmount"] = round(value, 2)
    return kwargs.get("sgstAmount")

def cgstAmount(firm: Firm, **kwargs) -> float:
    if not kwargs.get("cgstAmount"):
        total = amount(firm, **kwargs)
        value = (cgst(firm) * total) / 100
        kwargs["cgstAmount"] = round(value, 2)
    return kwargs.get("cgstAmount")

def roundOff(firm: Firm, **kwargs) -> float:
    if not kwargs.get("roundOff"):
        amount_before_round_off = amount(firm, **kwargs)
        amount_before_round_off += sgstAmount(firm, **kwargs)
        amount_before_round_off += cgstAmount(firm, **kwargs)
        difference = math.ceil(amount_before_round_off) - amount_before_round_off
        kwargs["roundOff"] = round(difference, 2)
    return kwargs.get("roundOff")

def amountInWords(firm: Firm, **kwargs) -> float:
    if not kwargs.get("amountInWords"):
        tamount = int(totalAmount(firm, **kwargs))
        kwargs["amountInWords"] = "RUPEES " + convert_to_words(tamount)
    return kwargs.get("amountInWords")

def get_table_1_header(cols: list[dict]) -> str:
    """<thead class="table-secondary">
        <tr>
          <th scope="col" id="serialNumber">Sr. No</th>
          <th scope="col" id="size">SIZE</th>
          <th scope="col" id="description">DESCRIPTION</th>
          <th scope="col" id="quantity">QUANT</th>
          <th scope="col" id="unit">Unit</th>
          <th scope="col" id="hsnCode">HSN Code</th>
          <th scope="col" id="amount">Amount</th>
        </tr>
        </thead>"""
    ths = ""
    for col in cols:
        col_id = col.get("field")
        col_name = col.get("description")
        ths += f'<th scope="col" id="{col_id}">{col_name}</th>'
    return f'<thead class="table-secondary"><tr>{ths}</tr></thead>'

def get_row_element(row: dict, col_names: list[str]):
    tds = ""
    for col in col_names:
        tds += f'<td>{row.get(col)}</td>'
    return f'<tr>{tds}</tr>'


def get_table_1_body(rows: list[dict], column_details: list[dict]) -> str:
    col_names = []
    trs = ""
    total = 0
    for col_name in column_details:
        col_names.append(col_name.get("field"))
    for row in rows:
        trs += get_row_element(row, col_names)
        total += float(row.get("amount"))
    trs += f'<tr><td colspan="{len(col_names)-1}">Total</td><td>{total}</td></tr>'
    return f'<tbody>{trs}</tbody>'

def table1(firm: Firm, **kwargs) -> str:
    if not kwargs.get("table1"):
        column_details = firm.get_invoice_template()["Table Details"]
        header = get_table_1_header(column_details)
        body = get_table_1_body(kwargs.get("Table Details"), column_details)
        kwargs["table1"] = f"{header}{body}"
    return kwargs.get("table1")

def get_value(field_name: str, company_id: str, **kwargs):
    if kwargs.get(field_name):
        return kwargs.get(field_name)
    firm: Firm = Firm.query.get(company_id)
    if field_name in globals():
        return globals()[field_name](firm, **kwargs)
    else:
        print(f"{field_name} not found in value getter, for company id: {company_id}")
        return None