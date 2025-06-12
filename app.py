from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:200274@localhost/project-oo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from models.user import User
        db.create_all()

        # ✅ Registrar o blueprint
        from controller.user_controller import user_bp
        app.register_blueprint(user_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
