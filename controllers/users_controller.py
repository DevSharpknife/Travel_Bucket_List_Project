from flask import Blueprint, Flask, render_template, redirect, request

from models.user import User
import repos.user_repo as user_repo

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repo.select_all()
    return render_template("users/index.html", users=users)

# NEW - CREATE
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html")

@users_blueprint.route("/users", methods=["POST"])
def create_user():
    name = request.form["new_user_name"]
    age = request.form["new_user_age"]
    new_user = User(name, age)
    user_repo.save(new_user)
    users = user_repo.select_all()
    return render_template("users/index.html", users=users)

# EDIT - UPDATE
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repo.select(id)
    return render_template("/users/edit.html", user=user)

@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    name = request.form["updated_user_name"]
    age = request.form["updated_user_age"]
    updated_user = User(name, age, id)
    user_repo.update(updated_user)
    return redirect("/users")

# REMOVE - DELETE
@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user_repo.delete(id)
    return redirect("/users")
