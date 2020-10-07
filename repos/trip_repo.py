from db.run_sql import run_sql
from models.trip import Trip
from models.user import User
from models.city import City
import repos.user_repo as user_repo
import repos.city_repo as city_repo

def save(trip):
    sql = "INSERT INTO trips ( user_id, name, city_id, date, duration, review ) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [trip.user.id, trip.name, trip.city.id, trip.date, trip.duration, trip.review]
    results = run_sql(sql, values)
    id = results[0]['id']
    trip.id = id

def select_all():
    trips = []
    sql = "SELECT * FROM trips"
    results = run_sql(sql)
    for row in results:
        user = user_repo.select(row['user_id'])
        city = city_repo.select(row['city_id'])
        trip = Trip(user, row['name'], city, row['date'], row['duration'], row['review'])
        trips.append(trip)
    return trips

def select(id):
    sql = "SELECT * FROM trips WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = user_repo.select(result['user_id'])
        city = city_repo.select(result['city_id'])
        trip = Trip(user, result['name'], city, result['date'], result['duration'], result['review'], result['id'])
    return trip

def delete_all():
    sql = "DELETE FROM trips"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM trips WHERE id = %s"
    values = [id]
    run_sql(sql, values)
