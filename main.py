import os
APP_DIR = os.path.dirname(os.path.abspath(__file__))
os.sys.path.append(os.path.join(APP_DIR, 'vendor'))
os.sys.path.append(os.path.join(APP_DIR, 'src'))

import click
from gsheet2csv import google_sheet_to_csv
from pathlib import Path

@click.command()
@click.option('--credentials', required=True, default='credentials.json', help='Credentials file')
@click.option('--sheet_key', required=True, help='Sheet key')
@click.option('--worksheet', required=True, help='Worksheet')
def main(credentials: str, sheet_key: str, worksheet: str):
    google_sheet_to_csv(
        Path(credentials),
        sheet_key,
        worksheet
    )


if __name__ == '__main__':
    main()
