#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table(
        'place_amenity', Base.metadata, Column(
            'place_id', String(60), ForeignKey(
                'places.id'), primary_key=True, nullable=False), Column(
                    'amenity_id', String(60), ForeignKey(
                        'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    reviews = relationship("Review", backref='place', cascade="all, delete")
    amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)

    @property
    def reviews(self):
        """
        Returns the list of review instances with place_id == place_id
        """
        from models import storage
        my_list = []
        fetched_reviews = storage.all('Review').values()
        for review in fetched_reviews:
            if self.id == review.place_id:
                my_list.append(review)
        return my_list

    @property
    def amenities(self):
        """
        Returns the list of amenity instances based on the attribute amenity_id
        that contains all ameniti_id's linked to that Place
        """
        from models import storage
        my_list = []
        fetched_amenities = storage.all('Amenity').values()
        for amenity in fetched_amenities:
            if self.id == amenity.amenity_ids:
                my_list.append(amenity)
        return my_list

    @amenities.setter
    def amenities(self, obj):
        """
        Handle append method for adding amenity.id to the attribute amenity_ids
        """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
