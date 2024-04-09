from typing import List
from model.user import User
from repository.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: List[User] = []

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def get_user(self, username: str) -> User | None:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update_user(self, username: str, user_data: User) -> User | None:
        for i, user in enumerate(self.users):
            if user.username == username:
                self.users[i] = user_data
                return user_data
        return None

    def delete_user(self, username: str) -> None:
        for i, user in enumerate(self.users):
            if user.username == username:
                del self.users[i]
                return
        raise ValueError(f"User with username {username} not found")
