from models.user import User

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_user(self, user_id):
        return self.user_repo.get_by_id(user_id)

    def create_user(self, nome, email):
        user = User(nome=nome, email=email)
        self.user_repo.add(user)
        return user
