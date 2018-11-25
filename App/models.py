from sqlalchemy import Column, Integer, Float, String
from database import Base
import json

class Organisation(Base):
    __tablename__ = 'organisation'
    id = Column(Integer, primary_key=True)
    organisation = Column(String(50), unique=True)
    address = Column(String(500), unique=True)
    website = Column(String(120), unique=True)
    about = Column(String(1000), unique=True)
    email = Column(String(120), unique=True)
    twitter = Column(String(120), unique=True)
    phone_number = Column(String(120), unique=True)
    latitude = Column(Float, unique=True)
    longitude = Column(Float, unique=True)

    def __init__(self, organisation=None, address=None, website=None, about=None, email=None, twitter=None, phone_number=None, latitude=None, longitude=None):
        self.organisation = organisation
        self.address = address
        self.website = website
        self.about = about
        self.email = email
        self.twitter = twitter
        self.phone_number = phone_number
        self.latitude = latitude
        self.longitude = longitude
    

    def __repr__(self):
        return '<Organisation %r>' % (self.name)


class Service:
    def __init__(self, query):
        self.organisation = query[1]
        self.address = query[2]
        self.website = query[3]
        self.about = query[4]
        self.email = query[5]
        self.twitter = query[6]
        self.phone_number = query[7]
        self.lat = query[8]
        self.long = query[9]


    def query_as_json(self):
        d = {}
        d['organisation'] = self.organisation
        d['address'] = self.address
        d['website'] = self.website
        d['about'] = self.about
        d['email'] = self.email
        d['twitter'] = self.twitter
        d['phone_number'] = self.phone_number
        d['lat'] = self.lat
        d['long'] = self.long
        return json.dumps(d)

