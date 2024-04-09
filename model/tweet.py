from pydantic import BaseModel
from datetime import datetime


class Tweet(BaseModel):
    id: int
    content: str
    created_at: datetime
    username: str
