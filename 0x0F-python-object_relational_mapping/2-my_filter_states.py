#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Selects and prints all states from the specified database
    where the name matches the provided state_name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    c = db.cursor()

    # Format the SQL query with the user input
    query = ("SELECT * FROM states "
             "WHERE name = %s ORDER BY id ASC")

    # Execute SQL query
    c.execute(query, (state_name,))

    # Fetch all rows and print them
    for row in c.fetchall():
        print(row)

    # Close the cursor and disconnect from server
    c.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_states(username, password, database, state_name)
    else:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
