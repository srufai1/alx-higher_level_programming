#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .relationship_city import Base  # Updated import

class State(Base):
    """
    State class linked to the 'states' table.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

from .relationship_city import City  # Moved import to the end

