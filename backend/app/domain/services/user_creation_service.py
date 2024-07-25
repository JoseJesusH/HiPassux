# app/domain/services/user_creation_service.py
from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

class UserCreationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username, first_name, last_name, birth_date, phone_number, gender, email, password):
        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone_number=phone_number,
            gender=gender,
            email=email,
            password=password
        )
        self.user_repository.add_user(new_user)
