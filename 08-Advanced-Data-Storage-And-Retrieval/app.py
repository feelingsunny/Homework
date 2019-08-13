import sqlalchemy
import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

print (Base.classes.keys())

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#Init app
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    # List all available api routes.""""
    return (
        "Available Routes for climate analysis!<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/start<br/>"
        "/api/v1.0/start/end"
)

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Convert the query results to a Dictionary using date as the key and prcp as the value

    # Calculate the date 1 year ago from latest_data
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_scores = session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date > one_year_ago).all()

    # Convert list of tuples into normal list
    precipitation_dict = dict(precipitation_scores)

    #Return the JSON representation of your dictionary.
    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations(): 
    # Query stations
    stations =  session.query(Measurement.station).group_by(Measurement.station).all()

    # Convert list of tuples into normal list
    stations_list = list(np.ravel(stations))

    #Return a JSON list of stations from the dataset.
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Query for the dates and temperature observations from a year from the last data point.

    # Calculate the date 1 year ago from latest_data
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    
    # Perform a query to retrieve the data and precipitation scores
    tobs = session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.date > one_year_ago).all()

    # Convert list of tuples into normal list
    tobs_list = list(tobs)
    
    # Return a JSON list of Temperature Observations (tobs) for the previous year.  
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start_date(start):
    #Given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date. 
    from_start = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).group_by(Measurement.date).all()
        
    # Convert list of tuples into normal list
    from_start_list = list(np.ravel(from_start))

    # Return a JSON list of tmin, tmax, tavg for the dates greater than or equal to the date provided
    return jsonify(from_start_list)
         
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    #When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    Range_dates = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    
    # Convert list of tuples into normal list
    Range_dates_list=list(np.ravel(Range_dates))

    # Return a JSON list of tmin, tmax, tavg for the dates in range of start date and end date inclusive    
    return jsonify(Range_dates_list)


#Run Server
if __name__ == '__main__':
    app.run(debug=True)