import pdb

from models.trip import Trip
from models.user import User
from models.country import Country
from models.city import City
import repos.user_repo as user_repo
import repos.country_repo as country_repo
import repos.city_repo as city_repo
import repos.trip_repo as trip_repo

user_repo.delete_all()

user_1 = User('Maggie', 60)
user_repo.save(user_1)

user_2 = User('Vehan', 55)
user_repo.save(user_2)

user_3 = User('Victoria', 17)
user_repo.save(user_3)

country_1 = Country('Scotland')
country_repo.save(country_1)

country_2 = Country('England')
country_repo.save(country_2)

country_3 = Country('Northern Ireland')
country_repo.save(country_3)

city_1 = City('Belfast', country_3)
city_repo.save(city_1)

city_2 = City('London', country_2)
city_repo.save(city_2)

city_3 = City('Edinburgh', country_1)
city_repo.save(city_3)

city_4 = City('Glasgow', country_1)
city_repo.save(city_4)

trip_1 = Trip(user_1, "COVID GETAWAY", city_2, 16072020, 7, "Hated it. Too many people wearing masks. I like when I can see people's faces.")
trip_repo.save(trip_1)

trip_2 = Trip(user_1, "Northern Irish Xmas Trip", city_1, 20122019, 7, "Too Christmassy and I couldn't understand a word anyone was saying. My husband couldn't make it though so that was a bonus.")
trip_repo.save(trip_2)

trip_3 = Trip(user_3, "Christmas Hook Up", city_3, 21122019, 5, "Was great at first, away from my wife over the Christmas holidays, but the person I went to meet was not as happy to see me as I'd hoped she would be.")
trip_repo.save(trip_3)

trip_4 = Trip(user_2, "Meeting my new man", city_3, 21122019, 5, "Got catfished by an old man cheating on his wife. Love the Xmas markets though!")
trip_repo.save(trip_4)


pdb.set_trace()