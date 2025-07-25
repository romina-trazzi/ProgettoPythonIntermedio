from flask import Flask, render_template
from config import Config
from app.utilis.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app.views.web_routes import web_bp
        from app.views.api_routes import api_bp
        app.register_blueprint(web_bp)
        app.register_blueprint(api_bp)

        # Import models to ensure they are known to SQLAlchemy
        from app.models import review, product, user, purchase

        # Create database tables if they don't exist
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)