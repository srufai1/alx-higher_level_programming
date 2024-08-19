#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .relationship_state import Base  # Updated import

class City(Base):
    """
    City class linked to the 'cities' table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

from .relationship_state import State  # Moved import to the end

