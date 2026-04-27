"""Entry point for the application."""

import sys
from pathlib import Path

from .config import Config, ConfigurationError
from .reddit_client import RedditClient
from .fetcher import Fetcher
from .formatter import Formatter


def main():
    """Run the main application."""
    print("Rarchive v2.0")
    print("-" * 40)

    try:
        config = load_config()
    except ConfigurationError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)

    subreddit = get_subreddit_name()

    print(f"\nFetching posts from r/{subreddit}...")

    try:
        client = RedditClient(config)
    except Exception as e:
        print(f"Failed to connect to Reddit: {e}")
        sys.exit(1)

    fetcher = Fetcher(
        client=client,
        limit=config.post_limit,
        progress_callback=lambda idx, title: print(f"[{idx}] {title[:50]}"),
    )

    try:
        result = fetcher.fetch_posts(subreddit)
    except Exception as e:
        print(f"Failed to fetch posts: {e}")
        sys.exit(1)

    print(f"\nFetched {len(result.posts)} posts")

    formatter = Formatter(output_dir=config.output_dir or "output")
    try:
        output_path = formatter.save_fetch_result(result)
        print(f"Saved to: {output_path}")
    except Exception as e:
        print(f"Failed to save results: {e}")
        sys.exit(1)

    print("\nDone!")


def load_config() -> Config:
    """Load configuration from environment."""
    env_path = Path.cwd() / ".env"
    if env_path.exists():
        return Config.from_env(env_path)
    return Config.from_env()


def get_subreddit_name() -> str:
    """Get subreddit name from user input."""
    while True:
        name = input("Enter subreddit name: ").strip()
        if name:
            return name
        print("Please enter a subreddit name.")


if __name__ == "__main__":
    main()