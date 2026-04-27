"""Post fetching logic."""

from typing import Callable, Optional

from .models import Post, FetchResult
from .reddit_client import RedditClient


SortType = Optional[str]


SORT_METHODS = {
    "new": "new",
    "hot": "hot",
    "top": "top",
    "rising": "rising",
    "controversial": "controversial",
}


class Fetcher:
    """Handles fetching posts from Reddit."""

    def __init__(
        self,
        client: RedditClient,
        limit: int = 100,
        progress_callback: Optional[Callable[[int, str], None]] = None,
    ):
        """Initialize the fetcher."""
        self.client = client
        self.limit = limit
        self.progress_callback = progress_callback or self._default_progress

    @staticmethod
    def _default_progress(count: int, title: str) -> None:
        """Default progress callback."""
        print(f"[{count}] {title[:50]}...")

    def fetch_posts(
        self,
        subreddit_name: str,
        sort: SortType = "new",
    ) -> FetchResult:
        """Fetch posts from a subreddit."""
        subreddit = self.client.get_subreddit(subreddit_name)
        posts: list[Post] = []

        sort_method = SORT_METHODS.get(sort, "new")
        generator = getattr(subreddit, sort_method)(limit=self.limit)

        for idx, praw_post in enumerate(generator, 1):
            try:
                if self._is_valid_post(praw_post):
                    post = Post.from_praw_post(praw_post)
                    posts.append(post)
                    self.progress_callback(idx, post.title)
            except Exception:
                pass

        return FetchResult(
            posts=posts,
            subreddit=subreddit_name,
            sort_type=sort or "new",
        )

    def _is_valid_post(self, post) -> bool:
        """Check if a post should be included."""
        try:
            return bool(post.id)
        except Exception:
            return False