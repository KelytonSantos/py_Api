from extensions import db
from sqlalchemy import Numeric
from sqlalchemy import Enum as SQLEnum
from models.order_status import OrderStatus


class Product(db.Model):
    __tablename__ = 'Product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), primary_key=True)
    price = db.Column(Numeric(10,2), name='Price')

    order_lines = db.relationship('OrderLine', backref='product', lazy=True)
