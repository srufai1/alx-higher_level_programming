#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Lists all cities from the specified database that match
    the given state_name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cur = db.cursor()

    # Format the SQL query with the user input
    query = ("SELECT cities.name FROM cities "
             "INNER JOIN states ON states.id=cities.state_id "
             "WHERE states.name=%s ORDER BY cities.id ASC")

    # Execute SQL query with state_name as a parameter
    cur.execute(query, (state_name,))

    # Fetch all rows and print the results
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    # Close the cursor and disconnect from the server
    cur.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_cities(username, password, database, state_name)
    else:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
