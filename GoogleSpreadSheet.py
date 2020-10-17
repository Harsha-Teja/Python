"""
    creating a project. Then enable the google sheet api aswell. 

Before executing this script you have to visit the site console.cloud.google.com then go to googledrive api. Enable it while 
Upon enabling the googledrive api you will be redirected to the details page where a json file will be downloaded. In that json file 
    copy the client name and add that id in the sheet as shared to id. This will allow the sheet to be accessable by the script.
"""

# install this package to access the gsheets: pip install gspread oauth2client
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Mention the scope of the api being used: You can just copy these to use the google drive api and spreadsheet api
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# We have to input the creds we got from the google api json. Instead we are asking it to verify directly from the file we downloaded.
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# Asking it to authorize our sheet
client = gspread.authorize(creds)

# Opening the sheet we named as TeacherrDB and workingsheet number.
sheet = client.open("TeacherrDB").sheet1

# To get all the data from the sheet to print it here
data = sheet.get_all_records()
# printing the data. Wecan use the pprint (pretty print) package to print it in readable order
print(data)

# Inserting a row into the sheet. Same can be done to column as well.
insertrow = ["this", "is", "a", "test", "from", "googleapi"]

# Inserting command. The value to be inserted and the row number
sheet.insert_row(insertrow, 1)

# Getting specific row and column to print the value of that row or column here
row = sheet.row_values(3)
col = sheet.col_values(3)
# Same goes for cell as well with row, column values
cell = sheet.cell(3, 4).value

# updating the sheet where the row number is 3 and column number is 2 with the value "this is insane"
sheet.update_cell(3, 2, "This is insane")
