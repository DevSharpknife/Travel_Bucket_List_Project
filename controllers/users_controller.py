from flask import Blueprint, Flask, render_template, redirect, request

from models.user import User
import repositories.user_repository as user_repo

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


# REMOVE - DELETE

@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def delete_user(id):
    user_repo.delete(id)
    users = user_repo.select_all()
    return redirect("/users/index.html", users=users)
