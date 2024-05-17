import os
import pymysql
from openpyxl import load_workbook

# Database connection
database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    db="first_sikorsky"
)
cursor = database.cursor()


plane_model = "S-76"

cursor.execute("SELECT * FROM documents WHERE Aircraft_Model= %s",(plane_model,))

# Fetch all rows from the cursor
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# Display the rows with formatted output
for row in rows:
    print("Unique_ID:", row[0])
    print("doc_type:", row[1])
    print("Item_number:", row[2])
    # Continue for other columns
    print()
