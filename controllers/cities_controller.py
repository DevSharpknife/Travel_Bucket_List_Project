from flask import Blueprint, Flask, render_template, redirect, request

from models.city import City
from models.country import Country
import repos.city_repo as city_repo
import repos.country_repo as country_repo

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/cities")
def cities():
    cities = city_repo.select_all()
    return render_template("cities/index.html", cities=cities)

# NEW - CREATE
@cities_blueprint.route("/cities/new")
def new_city():
    return render_template("cities/new.html")

@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["new_city_name"]
    country = request.form["new_city_country"]
    new_country = Country(country)
    persistent_country = country_repo.save(new_country)
    new_city = City(name, persistent_country)
    city_repo.save(new_city)
    return redirect("/cities")

@cities_blueprint.route("/cities/<id>/edit")
def edit_city(id):
    city = city_repo.select(id)
    return render_template("/cities/edit.html", city=city)

@cities_blueprint.route()
def update_city(id):
    city_name = request.form["updated_city_name"]
    country_name = request.form["updated_country_name"]
    updated_city = City(city_name, country_name)


@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repo.delete(id)
    return redirect("/cities")
