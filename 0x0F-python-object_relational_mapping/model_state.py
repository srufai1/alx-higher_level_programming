#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


# Define the State class
class State(Base):
    """State class linked to the 'states' table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create a MySQL engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)
