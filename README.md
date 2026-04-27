# Subreddit Post Downloader

A Python script to archive posts from any public subreddit using Reddit's API via PRAW.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Reddit API](https://img.shields.io/badge/Reddit_API-TOS_compliant-orange)

---

## Features

- 📥 **Download Reddit Posts:** Retrieves posts along with important metadata such as title, author, score, etc.
- 🗂 **Organized Output:** Saves posts in JSON format with timestamps to easily track updates.
- ⏱ **Rate Limit Handling:** Automatically respects API rate limits.
- 📂 **Structured Directories:** Creates organized directories for the output.
- 🔒 **Reddit API Authentication:** Supports Reddit API authentication for secure requests.
- 🚫 **Robust Error Handling:** Properly handles errors for removed or deleted posts.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Binz120/subreddit-post-downloader.git
   cd subreddit-post-downloader
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**

   - **Create a Reddit App:**
     - Visit the [Reddit App Preferences](https://www.reddit.com/prefs/apps) page.
     - Click on "Create App" and choose the **"Script"** type.
     - Set the redirect URI to: `http://localhost:8080`

   - **Set up credentials:**
     - Create a `.env` file in the project root and add the following:

       ```env
       CLIENT_ID=your_client_id_here
       CLIENT_SECRET=your_client_secret_here
       USER_AGENT=script:subreddit-downloader:v1.0 (by /u/yourusername)
       ```

4. **Usage**

   Run the script with:

   ```bash
   python download_posts.py
   ```

   You will be prompted with:

   ```
   Enter subreddit name:
   ```

   For example, if you enter `python`, the output will be saved to a directory like:

   ```
   ./python_posts_<timestamp>/python_posts.json
   ```

---

## Sample Output

Below is an example of what the `python_posts.json` file might look like:

```json
[
  {
    "title": "Python 3.12 Released!",
    "author": "python_dev",
    "score": 15432,
    "created_utc": 1690843200,
    "url": "https://reddit.com/r/python/...",
    "num_comments": 892,
    "permalink": "/r/python/comments/...",
    "flair": "Official Announcement"
  }
]
```

---

## API Compliance

- **Respect Reddit's API Rules:**
  - The script uses a default limit of approximately 60 requests per minute.
  - Automatic rate limiting is implemented to handle API constraints.
  - For large-scale operations, consider adding manual delays to ensure compliance.
  - **Note:** Do not collect personal or private data. Always adhere to Reddit's API policies.

---

Happy archiving! If you have any questions or issues, feel free to open an issue on the repository.
