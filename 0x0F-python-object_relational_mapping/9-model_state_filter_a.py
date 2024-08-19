#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
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
    Lik_a = State.name.like('%a%')

    # Query to get all State objects and sort by id
    states_with_a = session.query(State).filter(Lik_a).order_by(State.id).all()

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
