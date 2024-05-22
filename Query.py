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

# Get user input safely
query = str(input("Please input the types of documents you will be looking for in the database: "))

# Prepare the SQL query using parameterized queries
sql = """
SELECT * FROM documents
WHERE MATCH(see_it) AGAINST(%s IN NATURAL LANGUAGE MODE);
"""

# Execute the query with parameter
cursor.execute(sql, (query,))

# Fetch all rows
rows = cursor.fetchall()

# Display the rows
entry_count = 1
for row in rows:
    print(f"--------------This is entry # {entry_count}----------------- ")
    print("\n")
    print("Unique_ID:", row[0])
    print("doc_type:", row[1])
    print("Item_number:", row[2])
    print("Index_1:", row[3])
    print("Index_2:", row[4])  # Assuming this was meant to be Index_2 instead of another Index_1
    print("Type:", row[5])
    print("Reference:", row[6])
    print("See_it:", row[7])
    print("Aircraft_Model:", row[8])
    print("Description:", row[9])
    print("Names:", row[10])
    print("Date:", row[11])
    print("Comment:", row[12])

    entry_count += 1
    print("\n")

# Close the connection
database.close()
