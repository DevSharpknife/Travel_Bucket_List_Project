from flask import Blueprint, Flask, render_template, redirect, request

from models.country import Country
import repos.country_repo as country_repo

countries_blueprint = Blueprint("countries", __name__)

# INDEX
@countries_blueprint.route("/countries")
def countries():
    countries = country_repo.select_all()
    return render_template("countries/index.html", countries=countries)

# NEW - CREATE
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html")

@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["new_country_name"]
    new_country = Country(name)
    country_repo.save(new_country)
    countries = country_repo.select_all()
    return render_template("/countries/index.html", countries=countries)

@countries_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repo.select(id)
    return render_template("/countries/edit.html", country=country)

@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["updated_country_name"]
    updated_country = Country(name, id)
    country_repo.update(updated_country)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repo.delete(id)
    return redirect("/countries")
