from fastapi import APIRouter, Body, HTTPException, Depends
from typing import List

from model.user import User

from service.user_service import UserService



class UserController:
    def __init__(self, user_service: UserService = Depends(UserService)):
        self.user_service = user_service
        self.router = APIRouter()
        self.router.add_api_route("/users", self.create_user, methods=["POST"])
        self.router.add_api_route("/users/{username}", self.get_user, methods=["GET"])
        self.router.add_api_route("/users/{username}", self.update_user, methods=["PUT"])
        self.router.add_api_route("/users/{username}", self.delete_user, methods=["DELETE"])


    def create_user(self, user: User) -> User:
        """Creates a new user."""
        return self.user_service.create_user(user)

    def get_user(self, username: str) -> User:
        """Retrieves a user by username."""
        user = self.user_service.get_user(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # Assuming UserService doesn't implement get_all_users (check your implementation)
    # @router.get("/users", response_model=List[User])
    # def get_all_users(self) -> List[User]:
    #   """Retrieves all users."""
    #   return self.user_service.get_all_users()

    def update_user(self, username: str, user_data: User = Body(...)) -> User:
        """Updates a user with new data."""
        return self.user_service.update_user(username, user_data)  # type: ignore

    def delete_user(self, username: str) -> None:
        """Deletes a user by username."""
        self.user_service.delete_user(username)
