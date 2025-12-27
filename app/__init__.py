from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gearguard.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp 
    from app.routes.dashboard import dashboard_bp
    from app.routes.calendar import calendar_bp
    from app.routes.equipment import equipment_bp
    from app.routes.kanban import kanban_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(calendar_bp)
    app.register_blueprint(equipment_bp)
    app.register_blueprint(kanban_bp)
    return app
