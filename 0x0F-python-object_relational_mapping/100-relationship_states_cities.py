#!/usr/bin/python3
"""
Inserts the State "California" with the City "San Francisco"
into the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create engine and bind Base to it
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create California state
    california = State(name="California")

    # Create San Francisco city
    san_francisco = City(name="San Francisco", state=california)

    # Add California state to the session
    session.add(california)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()

