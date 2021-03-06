from db.run_sql import run_sql
from models.country import Country

def save(country):
    duplicate_country = find_duplicates(country)
    if duplicate_country == None:
        sql = "INSERT INTO countries ( name ) VALUES ( %s ) RETURNING id"
        values = [country.name.capitalize()]
        results= run_sql(sql, values)
        id = results[0]['id']
        country.id = id
        return country
    else: 
        return duplicate_country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries

def select(id):
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['name'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)

def find_duplicates(new_country):
    countries_list = select_all()
    for country in countries_list:    
        if country.name == new_country.name.capitalize():
            return country
    return None


