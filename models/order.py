from extensions import db
from sqlalchemy import Numeric
from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo

class Order(db.Model):
    __tablename__ = 'Order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id'), name='CustomerID')
    customer = db.relationship('Customer', backref='orders')
    total_amount = db.Column(Numeric(10, 2), name = 'TotalAmount')
    order_date = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(ZoneInfo("America/Sao_Paulo"), name='OrderDate')
    )
    order_status_id = db.Column(db.Integer, db.ForeignKey('OrderStatus.id'), name='OrderStatusID')

    order_lines = db.relationship('OrderLine', backref='order', lazy=True)
