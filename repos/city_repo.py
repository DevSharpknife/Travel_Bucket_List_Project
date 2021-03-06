from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repos.country_repo as country_repo

def save(city):
    duplicate_city = find_duplicates(city)
    if duplicate_city == None:
        sql = "INSERT INTO cities ( name, country_id, visited ) VALUES ( %s, %s, %s ) RETURNING id"
        values = [city.name.capitalize(), city.country.id, city.visited]
        results = run_sql(sql, values)
        id = results[0]['id']
        city.id = id
        return city
    else:
        return duplicate_city

def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        country = country_repo.select(row['country_id'])
        city = City(row['name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = country_repo.select(result['country_id'])
        city = City(result['name'], country, result['visited'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def update(city):
#     sql = "UPDATE cities SET ( name, country ) = %s WHERE id = %s"
#     city_country = select(city.id)
#     values = [city.name, city.country.id, city.id]
#     run_sql(sql, values)

def find_duplicates(new_city):
    cities_list = select_all()
    for city in cities_list:
        if city.name == new_city.name.capitalize() and city.country.name == new_city.country.name.capitalize():
            return city
    return None

def visit(id):
    sql = "UPDATE cities SET visited = True WHERE id = %s"
    values = [id]
    run_sql(sql, values)