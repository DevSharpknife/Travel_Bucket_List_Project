from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repos.country_repo as country_repo

def save(city):
        sql = "INSERT INTO cities ( name, country_id, visited ) VALUES ( %s, %s ) RETURNING id"
        values = [city.name.capitalize(), city.country.id]
        results = run_sql(sql, values)
        id = results[0]['id']
        city.id = id

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], country, row['id'])
        cities.append(city)
    return cities

def select(id):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repo.select(result['country_id'])
        city = City(result['name'], country, result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(city):
    sql = "UPDATE cities SET ( name, country ) = %s WHERE id = %s"
    values = [city.name, city.country.id, city.id]
    run_sql(sql, values)
