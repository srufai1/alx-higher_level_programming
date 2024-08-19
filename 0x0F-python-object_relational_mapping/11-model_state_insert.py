#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_03_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine and bind Base to it
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State to the session
    session.add(new_state)

    # Commit the change to the database
    session.commit()

    # Print the new State's ID
    print(new_state.id)

    # Close the session
    session.close()
