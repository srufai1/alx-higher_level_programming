#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def cities_by_state(username, password, database):
    """
    Lists all cities from the specified database, sorted by id.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    c = db.cursor()

    # Execute SQL query to retrieve cities with corresponding states
    c.execute("SELECT cities.id, cities.name, states.name FROM cities "
              "JOIN states ON cities.state_id = states.id "
              "ORDER BY cities.id ASC")

    # Fetch all rows and print them
    for row in c.fetchall():
        print(row)

    # Close the cursor and disconnect from server
    c.close()
    db.close()


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        cities_by_state(username, password, database)
    else:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
