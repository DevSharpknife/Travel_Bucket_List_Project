from flask import Blueprint, Flask, render_template, redirect, request

from models.trip import Trip
import repositories.trip_repository as trip_repo
import repositories.country_repository as country_repo
import repositories.city_repository as city_repo

trips_blueprint = Blueprint("trips", __name__)

# INDEX
@trips_blueprint.route("/trips")
def trips():
    trips = trip_repo.select_all()
    return render_template("trips/index.html", trips=trips)

# NEW - CREATE
@trips_blueprint.route("/trips/new")
def new_trip():
    return render_template("trips/new.html")

@trips_blueprint.route("/trips", methods=["POST"])
def create_trip():
    name = request.form["new_trip_name"]
    age = request.form["new_trip_age"]
    new_trip = Trip(name, age)
    trip_repo.save(new_trip)
    return render_template("/trips")
