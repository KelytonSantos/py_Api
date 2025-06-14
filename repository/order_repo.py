from models.order import Order

class OrderRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, order_id):
        return self.db_session.query(Order).filter_by(id=order_id).first()

    def list_all(self):
        return self.db_session.query(Order).all()

    def add(self, order):
        self.db_session.add(order)
        self.db_session.commit()
