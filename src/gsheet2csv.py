import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
from pathlib import Path


def google_sheet_to_csv(credentials_path: Path, sheet_key: str, worksheet_name: str):

    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(str(credentials_path.resolve()), scope)
    gs = gspread.authorize(credentials)

    sheet = gs.open_by_key(sheet_key)
    worksheet = sheet.worksheet(worksheet_name)

    list(map(lambda x: print(*x, sep=','), worksheet.get_all_values()))
