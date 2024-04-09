from fastapi import Depends, FastAPI

from controller import tweet_controller, user_controller
from repository.implementation.in_memory_tweet_repository import InMemoryTweetRepository
from repository.implementation.in_memory_user_repository import InMemoryUserRepository
from service.tweet_service import TweetService
from service.user_service import UserService

user_repository = InMemoryUserRepository()
tweet_repository = InMemoryTweetRepository()

user_service = UserService(user_repository)
tweet_service = TweetService(tweet_repository)

app = FastAPI()


user_controller = user_controller.UserController(user_service)
tweet_controller = tweet_controller.TweetController(tweet_service)

user_router = user_controller.router
tweet_router = tweet_controller.router

app.include_router(user_router)
app.include_router(tweet_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
