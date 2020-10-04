from flask import Blueprint, Flask, render_template

from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    humans = user_repository.select_all()
    return render_template("users/index.html", users=users)