from typing import List

from model.user import User


class UserRepository:
    def create_user(self, user: User) -> User:  # type: ignore
        """Creates a new user and returns the created user."""
        pass

    def get_user(self, username: str) -> User | None:  # type: ignore
        """Retrieves a user by username."""
        pass

    def update_user(self, username: str, user_data: User) -> User | None:  # type: ignore
        """Updates a user with new data."""
        pass

    def delete_user(self, username: str) -> None:
        """Deletes a user by username."""
        pass
