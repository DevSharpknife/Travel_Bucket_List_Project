import pdb

from models.user import User
from models.country import Country
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository

user_repository.delete_all()

user_1 = User('Maggie', 60)
user_repository.save(user_1)

user_2 = User('Vehan', 55)
user_repository.save(user_2)

user_3 = User('Victoria', 17)
user_repository.save(user_3)

country_1 = Country('Scotland')
country_repository.save(country_1)

country_2 = Country('England')
country_repository.save(country_2)

country_3 = Country('Ireland')
country_repository.save(country_3)

pdb.set_trace()