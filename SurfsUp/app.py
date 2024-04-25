# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# print(engine)

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`


# Create a session


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return(
        f"Welcome to the climate API!<br/>"
        f"<br/>"
        f"Available routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/<start><br/>"
        f"<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

"""
@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(

@app.route("/api/v1.0/<start>")
def start():
    return jsonify(

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return jsonify()
"""
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)