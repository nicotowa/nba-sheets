from __future__ import print_function
from pprint import pprint

import os.path
import httplib2

from apiclient import discovery
from google.oauth2 import service_account

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1_ZizDlHqPoS9xtPiHWjMnyeeNVsqiz7Ih6xlSClOYKc'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'
SAMPLE_RANGE_NAME = 'A1:M'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = service_account.Credentials.from_service_account_file("./credentials.json", scopes=SCOPES)
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        pprint(values)
        # print('Name, Major:')
        # for row in values:
        #     # Print columns A and E, which correspond to indices 0 and 4.
        #     print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()