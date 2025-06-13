from extensions import db

class Customer(db.Model):
    __tablename__ = 'Customer'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)