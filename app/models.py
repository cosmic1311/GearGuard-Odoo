# Later you will add SQLAlchemy here
from datetime import datetime
from app import db
from flask_login import UserMixin

class Request(db.Model):
    __tablename__ = "requests"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    status = db.Column(
        db.String(20),
        default="pending",   # pending | approved | rejected | completed
        nullable=False
    )

    priority = db.Column(
        db.String(20),
        default="medium",    # low | medium | high
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Request {self.id} - {self.title}>"



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
