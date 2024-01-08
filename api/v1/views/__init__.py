#!/usr/bin/pyhon3
'''the blueprint for the API.'''
from flask import Flask, Blueprint

app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *
from api.v1.views.index import *
