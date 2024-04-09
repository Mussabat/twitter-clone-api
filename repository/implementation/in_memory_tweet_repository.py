from typing import List
from model.tweet import Tweet
from repository.tweet_repository import TweetRepository


class InMemoryTweetRepository(TweetRepository):
  def __init__(self):
    self.tweets: List[Tweet] = []

  def create_tweet(self, tweet: Tweet) -> Tweet:
    self.tweets.append(tweet)
    return tweet

  def get_tweet(self, tweet_id: int) -> Tweet | None:
    for tweet in self.tweets:
      if tweet.id == tweet_id:
        return tweet
    return None

  def get_all_tweets(self) -> List[Tweet]:
    return self.tweets.copy()

  def get_user_tweets(self, username: str) -> List[Tweet]:
    return [tweet for tweet in self.tweets if tweet.username == username]

  def update_tweet(self, tweet_id: int, tweet_data: Tweet) -> Tweet | None:
    for i, tweet in enumerate(self.tweets):
      if tweet.id == tweet_id:
        self.tweets[i] = tweet_data
        return tweet_data
    return None

  def delete_tweet(self, tweet_id: int) -> None:
    for i, tweet in enumerate(self.tweets):
      if tweet.id == tweet_id:
        del self.tweets[i]
        return
    raise ValueError(f"Tweet with id {tweet_id}")