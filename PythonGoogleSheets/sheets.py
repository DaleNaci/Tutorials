import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("tutorial").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(1, 2).value

# pprint(cell)

insertRow = ["hello", 5, "red", "blue"]
# sheet.insert_row(row, 4)
# sheet.delete_rows(4)
# sheet.update_cell(2, 2, "changed")
numRows = sheet.row_count

print(len(data))
