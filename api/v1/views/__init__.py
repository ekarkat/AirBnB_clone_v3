#!/usr/bin/pyhon3
'''the blueprint for the API.'''
from flask import Flask, Blueprint

app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *
""" this is for state"""
from api.v1.views.states import *
""" this is for state"""
# from api.v1.views.cities import *
""" this is for state"""
# from api.v1.views.amenities import *
""" this is for state"""
# from api.v1.views.users import *
