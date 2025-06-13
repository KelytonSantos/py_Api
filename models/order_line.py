from extensions import db

class OrderLine(db.Model):
    __tablename__ = 'OrderLine'

    order_line_id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('Order.id'), name = 'OrderID')
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), name = "ProductID")
    quantity = db.Column(db.Integer)