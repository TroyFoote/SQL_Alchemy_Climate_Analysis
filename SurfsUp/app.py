# Import Flask
from flask import Flask, jsonify
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect the database
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

  


#Flask set up

#Create app
app = Flask(__name__)

#Flask routes

@app.route("/")
def welcome():
    """List all available API routes."""
    print("Server received request for welcome page")
    return (
        f"Available Routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for precipitation page")
    # Create session from python to database
    session = Session(engine)

    #Convert the query results to a dictionary by using date as the key and prcp as the value.
    past_year_precipitation = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    all_data = []
    for date, prcp in past_year_precipitation:
        data_dict ={}
        data_dict['date'] = date
        data_dict['prcp'] = prcp
        all_data.append(data_dict) 

    return jsonify(all_data)


@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for stations page")
    # Create session from python to database
    session = Session(engine)
    
    #Return a JSON list of stations from the dataset.
    station_names =session.query(Station.station, Station.name).all()
    
    session.close()

    #Convert list of tuples into a normal list
    stations_list = list(np.ravel(station_names))

    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for tobs page")
    # Create session from python to database
    session = Session(engine)

    #Query the dates and temperature observations of the most-active station for the previous year of data.
    
    #find most active station
    active_stations =session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).first()
    
    most_active_station_id = active_stations[0]
    print(f"The most active station is {most_active_station_id}")

    most_recent_row =session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_str =most_recent_row[0]
    most_recent_date = dt.date.fromisoformat(most_recent_str)
    print("Most Recent Date: ", most_recent_date)

    #find date from a year ago
    query_date = most_recent_date - dt.timedelta(days=365)
    print("Query Date: ", query_date)
    
    last_year = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == most_active_station_id).\
    filter(Measurement.date >=query_date).all()

    session.close()

    #Convert list of tuples into a normal list
    tobs_list = list(np.ravel(last_year))

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(specified_start_date):
    """Fetch the TMIN, TMAX and TAVG for all dates greater than or equal to the start date."""
    print("Server received request for start page")
    
    # Create session from python to database
    session = Session(engine)

    #Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    #For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    
       # canonicalised = superhero.replace(" ", "").lower()
    # for character in justice_league_members:
    #     search_term = character["superhero"].replace(" ", "").lower()

    #     if search_term == canonicalised:
    #         return jsonify(character)

    # return jsonify({"error": "Character not found."}), 404



    #For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
   

    session.close()


if __name__ == "__main__":
    app.run(debug=True)


