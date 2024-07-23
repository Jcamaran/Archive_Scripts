import requests
import json
import datetime
from openpyxl import load_workbook

# Constants for API for Monday.com
apiKey = "YOUR_API_KEY"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}


# Path to Excel file
EXCEL_PATH = r"YOUR_PATH_TO_EXCEL FOLDERS"



def load_excel(file_path):
    """Load the Excel workbook and return the workbook object."""
    return load_workbook(file_path, data_only=True)

def list_worksheets(workbook):
    """List all worksheet names in the workbook."""
    print("These are all the worksheets in the file: ")
    for index, sheetname in enumerate(workbook.sheetnames, start=1):
        print(f"{index}: {sheetname}")

def get_worksheet(workbook, sheet_name):
    """Get the specified worksheet from the workbook."""
    return workbook[sheet_name]

def get_all_rows(worksheet):
    """Get all rows from the specified worksheet."""
    return list(worksheet.rows)



def enter_data_from_excel(rows):
    for i, row in enumerate(rows[1:2], start=1):
        request_from = row[5].value
        request_number = row[0].value
        description = row[7].value
        due_date = row[8].value

        print(f"Row Number {i}: ")
        print(f"Request Number: {request_number}")
        print(f"Description: {description}")

        if isinstance(due_date, datetime.datetime):
            formatted_due_date = due_date.strftime('%Y-%m-%d')
            print(f"Due Date: {formatted_due_date}")

        # GraphQL mutation with variables
        importing_query = """
        mutation($board_id: ID!, $item_name: String!, $column_values: JSON!) {
          create_item(board_id: $board_id, item_name: $item_name, columnVals: $column_values) {
            id
          }
        }
        """
        variables = {
            "board_id": 6951881761,
            "item_name": f"Request:{request_from}",
            'columnVals' : json.dumps({
                'status' : {'label' : 'Done'},
                'date4' : {'date' : due_date}
            })
        }
        data = {'query': importing_query, 'variables': variables}

        # Make the request and handle the response
        try:
            response = requests.post(url=apiUrl, json=data, headers=headers)
            response_data = response.json()
            if 'errors' in response_data:
                print(f"Error creating item: {response_data['errors']}")
            else:
                print(f"Item created with ID: {response_data['data']['create_item']['id']}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")


def main():
    # Load the workbook and list all worksheets
    workbook = load_excel(EXCEL_PATH)
    list_worksheets(workbook)
    
    # Get the tracking worksheet and all its rows
    tracking_worksheet = get_worksheet(workbook, 'Tracking')
    all_rows = get_all_rows(tracking_worksheet)
    print(f"There are {len(all_rows)} rows of data in this excel sheet")

    # Print the first five entries
    # print_first_five_entries(all_rows)
    enter_data_from_excel(all_rows)

if __name__ == "__main__":
    main()
