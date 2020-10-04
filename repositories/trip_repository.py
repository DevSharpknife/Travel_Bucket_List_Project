from db.run_sql import run_sql
from models.trip import Trip
from models.user import User
from models.city import City
import repositories.user_repository as user_repository
import repositories.city_repository as city_repository

def save(trip):
    sql = "INSERT INTO trips ( user_id, city_id, date, duration, review ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [trip.user.id, trip.city.id, trip.date, trip.duration, trip.review]
    results = run_sql(sql, values)
    id = results[0]['id']
    trip.id = id

def select_all():
    trips = []
    sql = "SELECT * FROM trips"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['user_id'])
        city = city_repository.select(row['city_id'])
        trip = Trip(user, city, row['date'], row['duration'], row['review'])
        trips.append(trip)
    return trips


