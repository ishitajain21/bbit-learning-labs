"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT


# POST: pay , PUT: phone number
@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def format_article(article: dict) -> Article:
    """Format a dictionary into an Article object."""
    return Article(
        author=article["author"],
        title=article["title"],
        body=article["body"],
        publish_date=datetime.strptime(article["publish_date"], "%Y-%m-%d"),
        image_url=article["image_url"],
        url=article["url"],
    )


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    RedisClient = RedisClient()
    entrie = RedisClient.get_entry("all_articles")
    # 2. Format the data into articles
    entries = []
    for i in entrie:
        entries.append(format_article(i))

    # 3. Return a list of the articles formatted
    return [entries]


def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    RedisClient = RedisClient()
    entrie = RedisClient.get_entry("all_articles")
    l = []
    for i in entrie:
        l.append(format_article(i))
    l.sort(key=lambda x: x.publish_date, reverse=True)
    # 2. Return as a list of articles sorted by most recent date
    return l
