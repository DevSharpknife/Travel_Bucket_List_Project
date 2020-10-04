import pdb

from models.trip import Trip
from models.user import User
from models.country import Country
from models.city import City
import repositories.user_repository as user_repository
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.trip_repository as trip_repository

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

country_3 = Country('Northern Ireland')
country_repository.save(country_3)

city_1 = City('Belfast', country_3)
city_repository.save(city_1)

city_2 = City('London', country_2)
city_repository.save(city_2)

city_3 = City('Edinburgh', country_1)
city_repository.save(city_3)

city_4 = City('Glasgow', country_1)
city_repository.save(city_4)

trip_1 = Trip(user_1, city_2, 16072020, 7, "Hated it. Too many people wearing masks. I like when I can see people's faces.")
trip_repository.save(trip_1)

trip_2 = Trip(user_1, city_1, 20122019, 7, "Too Christmassy and I couldn't understand a word anyone was saying. My husband couldn't make it so that also sullied the experience.")
trip_repository.save(trip_2)

trip_3 = Trip(user_3, city_3, 21122019, 5, "Was great at first, but the person I went to meet was not as happy to see me as I'd hoped she would be.")
trip_repository.save(trip_3)

trip_4 = Trip(user_2, city_3, 21122019, 5, "Got catfished by a man cheating on his wife. Love the Xmas markets though!")
trip_repository.save(trip_4)


pdb.set_trace()