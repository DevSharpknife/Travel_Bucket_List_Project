from db.run_sql import run_sql
from models.user import User

def save(user):
    sql = "INSERT INTO users (name, age) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    human.id = id

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result['name'], result['age'])
        users.append(user)
    return users
