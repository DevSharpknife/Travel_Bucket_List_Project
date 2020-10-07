from flask import Blueprint, Flask, render_template, redirect, request

from models.trip import Trip
import repos.trip_repo as trip_repo
import repos.country_repo as country_repo
import repos.city_repo as city_repo

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

@trips_blueprint.route("/trips/<id>/delete", methods=["POST"])
def delete_trip(id):
    trip_repo.delete(id)
    return redirect("/trips")
