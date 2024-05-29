#  Archives Database Scripts

## Description
This repository contains SQL and Python scripts used for querying, inserting, and transferring data into the Sikorsky Archives database. These scripts are part of an internship project focused on managing and retrieving historical data related to Sikorsky Aircraft.

## Contents
The repository includes the following files:

- **Example_selects.sql**: SQL script containing sample SELECT queries to retrieve data from the `Aircraft` and `Engineers` tables.
- **Example_inserts.sql**: SQL script containing sample INSERT statements to add new records to the `Aircraft` and `Engineers` tables.
- **Query.py**: Python script that connects to an SQLite database and runs a specified SQL query.
- **transfer_script.py**: Python script that transfers data from Excel sheets to a MySQL database, creating necessary tables and inserting data into them.

## Installation
To use the scripts in this repository, you need to have SQLite, Python, MySQL, and the necessary Python libraries installed on your system.

1. **SQLite**:
   - Download and install SQLite from the [official website](https://www.sqlite.org/download.html).

2. **Python**:
   - Download and install Python from the [official website](https://www.python.org/downloads/).

3. **MySQL**:
   - Download and install MySQL from the [official website](https://dev.mysql.com/downloads/).

4. **Python Libraries**:
   - Install the required Python libraries using pip:
     ```sh
     pip install pymysql openpyxl
     ```

## Usage

### SQL Scripts
1. **Running SELECT Queries**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing `Example_selects.sql`.
   - Use the SQLite command line tool to execute the script:
     ```sh
     sqlite3 sikorsky_archives.db < Example_selects.sql
     ```

2. **Running INSERT Statements**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing `Example_inserts.sql`.
   - Use the SQLite command line tool to execute the script:
     ```sh
     sqlite3 sikorsky_archives.db < Example_inserts.sql
     ```

### Python Script
1. **Running the Python Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing `Query.py`.
   - Run the script using Python:
     ```sh
     python Query.py
     ```

### Transfer Script
1. **Setting Up the MySQL Database**:
   - Ensure MySQL is running and you have created a database (e.g., `first_sikorsky`).
   - Update the database connection parameters in the `transfer_script.py` to match your MySQL setup.

2. **Running the Transfer Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory containing `transfer_script.py`.
   - Run the script using Python:
     ```sh
     python transfer_script.py
     ```

   The script will create the necessary tables and insert data from the specified Excel files into the MySQL database.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please feel free to reach out.
