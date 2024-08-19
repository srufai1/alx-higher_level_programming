#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_03_6_usa
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

    # Placeholder
    lik_a = State.name.like('%a%')

    # Query to get all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).filter(lik_a).all()

    # Delete the State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the change to the database
    session.commit()

    # Close the session
    session.close()
