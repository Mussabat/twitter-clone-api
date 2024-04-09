from typing import List

from model.user import User
from repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user: User) -> User:
        """Creates a new user and returns the created user."""
        return self.user_repository.create_user(user)

    def get_user(self, username: str) -> User | None:
        """Retrieves a user by username."""
        return self.user_repository.get_user(username)

    def update_user(self, username: str, user_data: User) -> User | None:
        """Updates a user with new data."""
        return self.user_repository.update_user(username, user_data)

    def delete_user(self, username: str) -> None:
        """Deletes a user by username."""
        self.user_repository.delete_user(username)

    def get_all_users(self) -> List[User]:
        """Retrieves all users (implementation depends on UserRepository)."""
        # This method depends on the specific implementation of UserRepository.
        # InMemoryUserRepository doesn't have this method, so you might
        # need to modify it or add it to the interface if needed.
        raise NotImplementedError("get_all_users not implemented in this base class")
