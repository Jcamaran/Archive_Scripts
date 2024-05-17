import os
import pymysql
from openpyxl import load_workbook

# Database connection
database = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Bigsuperguy21!@",
    db="first_sikorsky"
)
cursor = database.cursor()


plane_model = "S-76"

cursor.execute("SELECT * FROM documents WHERE Aircraft_Model= %s",(plane_model,))



# Define the SQL query string
# sql_query = """
# SELECT d.*, am.model_name AS Aircraft_Model_Name, dt.doc_type AS Document_Type
# FROM documents AS d
# JOIN aircraft_model_table AS am ON d.Aircraft_Model = am.model_name
# JOIN doc_type_table AS dt ON d.doc_type = dt.doc_type
# WHERE d.Aircraft_Model = 'S-76';
# """

# Execute the SQL query
# cursor.execute(sql_query)


# Fetch all rows from the cursor
rows = cursor.fetchall()

# Display the rows


entry_count = 1
for row in rows:
    print(row)

# Display the rows with formatted output
for row in rows:
    print(f"--------------This is entry # {entry_count}----------------- ")
    print("\n")
    print("Unique_ID:", row[0])
    print("doc_type:", row[1])
    print("Item_number:", row[2])
    print("Index_1:",row[3])
    print("Index_1:",row[4])
    print("Type:",row[5])
    print("Reference:",row[6])
    print("See_it:",row[7])
    print("Aircraft_Model:",row[8])
    print("Description:",row[9])
    print("Names:", row[10])
    print("Date:", row[11])
    print("Comment:", row[12])

    entry_count += 1
    print("\n")
