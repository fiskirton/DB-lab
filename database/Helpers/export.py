import pyexcel as pe


def save_xlsx(filepath, headers, data):
    sheet = pe.Sheet([headers])
    sheet.extend_rows(data)
    sheet.save_as(filepath)
