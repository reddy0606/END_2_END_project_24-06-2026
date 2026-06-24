import openpyxl


def get_data(path, sheet):
    workbook = openpyxl.load_workbook(path)
    sh = workbook[sheet]

    data = []
    for row in sh.iter_rows(values_only=True):
        data.append(row)

    return data