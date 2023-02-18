# Import Flask
from flask import Flask, jsonify
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, inspect, func


#Create app
app = Flask(__name__)

@app.route("/")
def index():
    return "Homepage"


@app.route("/api/v1.0/precipitation")
def precipitation():


@app.route("/api/v1.0/stations")
def stations():


@app.route("/api/v1.0/tobs")
def tobs():    