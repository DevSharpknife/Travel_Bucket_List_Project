from flask import Blueprint, Flask, render_template, redirect, request

from models.city import City
import repositories.city_repository as city_repo
import repositories.country_repository as country_repo

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
    new_city = City(name, country)
    city_repo.save(new_city)
    return render_template("/cities")
