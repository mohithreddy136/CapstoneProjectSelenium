import openpyxl

def get_data_from_excel(file_path, sheet_name):
    """
    Reads test data from an Excel file.
    :param file_path: Path to the .xlsx file.
    :param sheet_name: Name of the sheet to read from.
    :return: A list of lists, where each inner list represents a row of data.
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        data = []
        # Start from the second row to skip the header
        for row in range(2, sheet.max_row + 1):
            row_data = []
            for col in range(1, sheet.max_column + 1):
                row_data.append(sheet.cell(row=row, column=col).value)
            data.append(row_data)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except KeyError:
        print(f"Error: The sheet named '{sheet_name}' was not found in the workbook.")
        return None
