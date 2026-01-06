from ..models.user import User
from ..extensions import db


def register_user(username, email, password):
    if not username or not email or not password:
        raise ValueError("All fields are required")

    existing = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()

    if existing:
        raise ValueError("User already exists")

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user


def find_user_by_email(email):
    return User.query.filter_by(email=email).first()
