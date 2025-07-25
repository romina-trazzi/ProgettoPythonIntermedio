from app.models.user import User
from app.utilis.database import db

class UserController:
    def register_user(self, user_data, session):
        # user_data dovrebbe essere un dict con username, email, password
        user = User(
            username=user_data.get('username'),
            email=user_data.get('email'),
            password=user_data.get('password')  # In produzione, cifra la password!
        )
        session.add(user)
        session.commit()
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

    def authenticate_user(self, username, password, session):
        user = session.query(User).filter_by(username=username, password=password).first()
        return user

    def create_access_token(self, data):
        # Dummy token per esempio
        return "dummy-token"

    def get_current_user(self):
        # Dummy user per esempio
        return {
            "id": 1,
            "username": "demo",
            "email": "demo@example.com"
        }