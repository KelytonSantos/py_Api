from models.product import Product

class ProductRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_by_id(self, product_id):
        return self.db_session.query(Product).filter_by(id=product_id).first()

    def list_all(self):
        return self.db_session.query(Product).all()

    def add(self, product):
        self.db_session.add(product)
        self.db_session.commit()
