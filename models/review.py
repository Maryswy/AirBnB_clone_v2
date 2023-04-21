#!/usr/bin/python3
"""Thisis the review class"""
importmodels
frommodels.base_model import BaseModel, Base
fromsqlalchemy import Column, String, ForeignKey


classReview(BaseModel, Base):
   """This is the class for Review
   Attributes:
       place_id: place id
       user_id: user id
       text: review description
   """
   __tablename__ = "reviews"



   place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
   user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
   text = Column(String(1024), nullable=False)

