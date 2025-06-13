from extensions import db

class OrderStatus(db.Model):
    __tablename__ = 'OrderStatus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    orders = db.relationship('Order', backref='order_status')
