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

    # Query to get the State object with id=2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit the change to the database
    session.commit()

    # Close the session
    session.close()
