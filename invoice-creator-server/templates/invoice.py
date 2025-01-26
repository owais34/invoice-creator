import json

default_template = {
    "General Information": [
        {"field": "companyLogo", "description": "Company Logo", "type": "autofill", "formAttributes": {"type": "file"}},
        {"field": "companyName", "description": "Company Name", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "companyDescription", "description": "Company Description", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "companyAddress", "description": "Company Address", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "companyPhone", "description": "Company Phone number", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "companyEmail", "description": "Company Email", "type": "autofill", "formAttributes": {"type": "email"}},
        {"field": "gstin", "description": "Company GSTIN Number", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "invoiceNumber", "description": "Invoice Number", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "invoiceDate", "description": "Invoice Date", "type": "form", "formAttributes": {"type": "date"}},
        {"field": "buyersRefNumber", "description": "Buyers Reference Number", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "dispatchThrough", "description": "Dispatch Through", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "lrNumberAndDate", "description": "LR No. & Date ", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "termsOfPayment", "description": "Terms of payment", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "customerName", "description": "Customer Name", "type": "form", "formAttributes": {"type": "text"}}
    ],
    "Table Details": [
        {"field": "serialNumber", "description": "Sr. No", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "size", "description": "Size", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "itemDescription", "description": "Item Description", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "quantity", "description": "Qty", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "unit", "description": "Unit", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "rate", "description": "Rate", "type": "form", "formAttributes": {"type": "text"}},
        {"field": "amount", "description": "Amount", "type": "form", "formAttributes": {"type": "number", "step": "0.01"}}
    ],
    "Table 2 Details": [
        {"field": "sgst", "description": "SGST", "type": "form", "formAttributes": {"type": "number", "step": "0.01"}},
        {"field": "igst", "description": "IGST", "type": "form", "formAttributes": {"type": "number", "step": "0.01"}},
        {"field": "roundOff", "description": "R/U", "type": "form", "formAttributes": {"type": "number", "step": "0.01"}}
    ],
    "Account Information": [
        {"field": "accountName", "description": "Account Name", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "accountNumber", "description": "Account Number", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "ifscCode", "description": "Ifsc Code", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "bankName", "description": "Bank Name", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "branchName", "description": "Branch Name", "type": "autofill", "formAttributes": {"type": "text"}}
    ],
    "Final Information": [
        {"field": "amountInWords", "description": "Amount in words", "type": "function", "functionDefinition": "numberToWords(totalAmount)", "formAttributes": {"type": "function"}},
        {"field": "companySignature", "description": "Company Signature", "type": "autofill", "formAttributes": {"type": "text"}},
        {"field": "thankMessage", "description": "Company Gratitude Message", "type": "autofill", "formAttributes": {"type": "text"}}
    ]
}


json_format_default_template = json.dumps(default_template)

