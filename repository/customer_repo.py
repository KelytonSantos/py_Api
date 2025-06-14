from models.customer import Customer

class CustomerRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, customer_id):
        return self.db_session.query(Customer).filter_by(id=customer_id).first()

    def list_all(self):
        return self.db_session.query(Customer).all()

    def add(self, customer):
        self.db_session.add(customer)
        self.db_session.commit()
