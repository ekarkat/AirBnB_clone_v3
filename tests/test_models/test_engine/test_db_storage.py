#!/usr/bin/python3
import unittest
from models import storage
import os
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy import Table
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models.amenity import Amenity


class DBStorage(unittest.TestCase):
    """test db_storage"""

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db", "not for file storage")
    def test_all(self):
        """test all"""
        all_obj = storage.all()
        self.assertIsInstance(all_obj, dict)
    

