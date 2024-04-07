import sqlite3

# defining function for retrieving table names
def getTableNames():
    # connect to db
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()

    # fetch table names
    cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cr.fetchall()

    # close connection
    conn.close()

    # get table names
    tableNames = [table[0] for table in tables]
    return tableNames

# defining function to fetch ALL data
def fetch_all_data(table_name):
    # connect to db
    conn = sqlite3.connect('QuizBowl.db')
    cr = conn.cursor()

    # fetch ALL data
    cr.execute(f"SELECT * FROM {table_name};")
    data = cr.fetchall()

    # close connection
    conn.close()

    return data

# defining function to get table names and data in output
def main():
    tableNames = getTableNames()
    print("Table Names:")
    for table_name in tableNames:
        print(table_name)
        print("Data:")
        data = fetch_all_data(table_name)
        for row in data:
            print(row)
        print()

# making sure the script is running as main function
if __name__ == "__main__":
    main()