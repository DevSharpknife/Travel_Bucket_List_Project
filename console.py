import pdb

from models.user import User
import repositories.user_repository as user_repository

user_1 = User('Maggie', 60)
user_repository.save(user_1)


pdb.set_trace()