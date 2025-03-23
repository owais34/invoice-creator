from settings import BASE_DIR

html_template = None
html_template_file_path = f"{BASE_DIR}/templates/dynamic_template.html"

def get_fields_from_html_template(template: str) -> set[str] | list[str]:
    fields = []
    current_field_name = ""
    is_recording_field_name = False
    for ch in template:
        if ch == "$" and not is_recording_field_name:
            is_recording_field_name = True
        elif ch == "$" and is_recording_field_name:
            is_recording_field_name = False
            if current_field_name not in fields:
                fields.append(current_field_name)
            current_field_name = ""
        elif is_recording_field_name:
            current_field_name+=ch
        else:
            pass
    return fields


def get_html_template():
    global html_template
    if html_template is None:
        with open(html_template_file_path, "r") as template:
            html_template = template.read()

    return html_template

def get_fields():
    return get_fields_from_html_template(get_html_template())


def convert_to_words(n):
    if n == 0:
        return "Zero"

    # Indian numbering system places
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    thousands = ["", "Thousand", "Lakh", "Crore"]

    # Helper function for numbers less than 1000
    def convert_below_1000(n):
        if n == 0:
            return ""
        elif n < 20:
            return units[n]
        elif n < 100:
            return tens[n // 10] + ('' if n % 10 == 0 else " " + units[n % 10])
        else:
            return units[n // 100] + " Hundred" + ('' if n % 100 == 0 else " and " + convert_below_1000(n % 100))

    # Split the number into groups of 1000 (Indian system)
    result = []
    place = 0
    while n > 0:
        if n % 1000 != 0:
            result.append(convert_below_1000(n % 1000) + ('' if thousands[place] == '' else " " + thousands[place]))
        n //= 1000
        place += 1

    return ' '.join(reversed(result))

