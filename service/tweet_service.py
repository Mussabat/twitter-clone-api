from typing import List

from model.tweet import Tweet
from repository.tweet_repository import TweetRepository

class TweetService:
  def __init__(self, tweet_repository: TweetRepository):
    self.tweet_repository = tweet_repository

  def create_tweet(self, tweet: Tweet) -> Tweet:
    """Creates a new tweet and returns the created tweet."""
    return self.tweet_repository.create_tweet(tweet)

  def get_tweet(self, tweet_id: int) -> Tweet | None:
    """Retrieves a tweet by its id."""
    return self.tweet_repository.get_tweet(tweet_id)

  def get_all_tweets(self) -> List[Tweet]:
    """Retrieves all tweets."""
    return self.tweet_repository.get_all_tweets()

  def get_user_tweets(self, username: str) -> List[Tweet]:
    """Retrieves all tweets for a specific user."""
    return self.tweet_repository.get_user_tweets(username)

  def update_tweet(self, tweet_id: int, tweet_data: Tweet) -> Tweet | None:
    """Updates a tweet with new data."""
    return self.tweet_repository.update_tweet(tweet_id, tweet_data)

  def delete_tweet(self, tweet_id: int) -> None:
    """Deletes a tweet by its id."""
    self.tweet_repository.delete_tweet(tweet_id)