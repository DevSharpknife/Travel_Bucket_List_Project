import pdb

from models.user import User
import repositories.user_repository as user_repository

user_repository.delete_all()

user_1 = User('Maggie', 60)
user_repository.save(user_1)

user_2 = User('Vehan', 55)
user_repository.save(user_2)

user_3 = User('Victoria', 17)
user_repository.save(user_3)


pdb.set_trace()