from typing import List
from model.tweet import Tweet


class TweetRepository:
    def create_tweet(self, tweet: Tweet) -> Tweet:  # type: ignore
        """Creates a new tweet and returns the created tweet."""
        pass

    def get_tweet(self, tweet_id: int) -> Tweet | None:
        """Retrieves a tweet by its id."""
        pass

    def get_all_tweets(self) -> List[Tweet]: # type: ignore
        """Retrieves all tweets."""
        pass

    def get_user_tweets(self, username: str) -> List[Tweet]: # type: ignore
        """Retrieves all tweets for a specific user."""
        pass

    def update_tweet(self, tweet_id: int, tweet_data: Tweet) -> Tweet | None:
        """Updates a tweet with new data."""
        pass

    def delete_tweet(self, tweet_id: int) -> None:
        """Deletes a tweet by its id."""
        pass
