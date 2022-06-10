
from app.infrastructure.persistence import storage
from app.domain.users import User


class UserManager():
    def obtainIdetification(user_id: str):
        userKeyword = storage.get_entity(user_id)
        currnetUser = User(userKeyword)
        full_name = currnetUser.name + " " + currnetUser.last_name
        cc = currnetUser.cc
        return {full_name, cc}
