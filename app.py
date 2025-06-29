from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:200274@localhost/project-oo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from models.user import User
        
        from models.order import Order
        from models.product import Product
        from models.order_line import OrderLine
        from models.customer import Customer
        from models.order_status import OrderStatus

        db.create_all()

        from controller.user_controller import user_bp
        from controller.product_controller import product_bp
        from controller.customer_controller import customer_bp

        app.register_blueprint(user_bp)
        app.register_blueprint(product_bp)
        app.register_blueprint(customer_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
