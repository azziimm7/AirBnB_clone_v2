#!/usr/bin/python3
"""This script contains review attributes """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey

class Review(BaseModel):
    """ Review class inherits from basemodel and base
    to store review information
    Attributes:
    place_id
    user_id
    text

    """

    __tablename__ = "reviews"
    place_id = Column(String(60), nullable=False, ForignKey("place.id")
    user_id = Column(String(60), nullable=False, ForignKey("user.id")
    text = Column(String(1024), nullable=False)
