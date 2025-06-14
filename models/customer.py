from extensions import db

class Customer(db.Model):
    __tablename__ = 'Customer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)