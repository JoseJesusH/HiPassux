# app/domain/services/user_retrieval_service.py
from app.domain.repositories.user_repository import UserRepository

class UserRetrievalService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()
