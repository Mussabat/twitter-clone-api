from fastapi import APIRouter, Body, HTTPException, Depends
from typing import List

from model.tweet import Tweet

from service.tweet_service import TweetService


class TweetController:
    def __init__(self, tweet_service: TweetService = Depends(TweetService)):
        self.tweet_service = tweet_service
        self.router = APIRouter()
        self.router.add_api_route("/tweets", self.create_tweet, methods=["POST"])
        self.router.add_api_route("/tweets/{tweet_id}", self.get_tweet, methods=["GET"])
        self.router.add_api_route(
            "/users/{username}/tweets", self.get_user_tweets, methods=["GET"]
        )
        self.router.add_api_route("/tweets", self.get_all_tweets, methods=["GET"])
        self.router.add_api_route(
            "/tweets/{tweet_id}", self.update_tweet, methods=["PUT"]
        )
        self.router.add_api_route(
            "/tweets/{tweet_id}", self.delete_tweet, methods=["DELETE"]
        )

    def create_tweet(self, tweet: Tweet) -> Tweet:
        """Creates a new tweet."""
        return self.tweet_service.create_tweet(tweet)

    def get_tweet(self, tweet_id: int) -> Tweet:
        """Retrieves a tweet by its id."""
        tweet = self.tweet_service.get_tweet(tweet_id)
        if not tweet:
            raise HTTPException(status_code=404, detail="Tweet not found")
        return tweet

    def get_user_tweets(self, username: str) -> List[Tweet]:
        """Retrieves all tweets for a specific user."""
        return self.tweet_service.get_user_tweets(username)

    def get_all_tweets(self) -> List[Tweet]:
        """Retrieves all tweets."""
        return self.tweet_service.get_all_tweets()

    def update_tweet(self, tweet_id: int, tweet_data: Tweet = Body(...)) -> Tweet:
        """Updates a tweet with new data."""
        return self.tweet_service.update_tweet(tweet_id, tweet_data)  # type: ignore

    def delete_tweet(self, tweet_id: int) -> None:
        """Deletes a tweet by its id."""
        self.tweet_service.delete_tweet(tweet_id)
