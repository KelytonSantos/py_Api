# repository/user_repo.py
from models.user import User

class UserRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, user_id):
        return self.db_session.query(User).filter_by(id=user_id).first()

    def list_all(self):
        return self.db_session.query(User).all()

    def add(self, user):
        self.db_session.add(user)
        self.db_session.commit()
