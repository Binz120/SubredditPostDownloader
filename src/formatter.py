"""Output formatting for posts."""

import json
import os
from datetime import datetime
from pathlib import Path

from .models import FetchResult


class Formatter:
    """Handles formatting and saving post data."""

    def __init__(self, output_dir: str = "output"):
        """Initialize the formatter."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)

    def save_fetch_result(self, result: FetchResult) -> Path:
        """Save fetch result to JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        subreddit = result.subreddit
        filename = f"{subreddit}_posts_{timestamp}.json"

        output_path = self.output_dir / filename
        self._ensure_output_dir(output_path)

        data = self._convert_for_json(result)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return output_path

    def save_to_directory(self, result: FetchResult, custom_dir: Path) -> Path:
        """Save fetch result to a specific directory."""
        custom_dir.mkdir(exist_ok=True, parents=True)

        filename = f"{result.subreddit}_posts.json"
        output_path = custom_dir / filename

        data = self._convert_for_json(result)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return output_path

    def _convert_for_json(self, result: FetchResult) -> dict:
        """Convert fetch result to JSON-serializable format."""
        return {
            "subreddit": result.subreddit,
            "sort_type": result.sort_type,
            "fetched_at": result.fetched_at,
            "post_count": len(result.posts),
            "posts": [post.to_dict() for post in result.posts],
        }

    def _ensure_output_dir(self, path: Path) -> None:
        """Ensure output directory exists."""
        path.parent.mkdir(exist_ok=True, parents=True)