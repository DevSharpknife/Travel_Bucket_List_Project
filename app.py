from flask import Flask, render_template

from controllers.trips_controller import trips_blueprint
from controllers.users_controller import users_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.countries_controller import countries_blueprint


app = Flask(__name__)

app.register_blueprint(users_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(trips_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()