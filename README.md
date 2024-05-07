# Reddit Comment Detector Bot

The Reddit Comment Detector Bot is a Python script that monitors a specified subreddit for comments containing a target phrase. When a comment matching the phrase is found, the bot can perform desired actions, such as replying to the comment or logging the details.

## Features

- Monitors a specified subreddit in real-time for new comments
- Detects comments containing a specific target phrase (case-insensitive)
- Prints the permalink of the matching comments
- Customizable actions to perform when a matching comment is found
- Handles authentication errors and provides informative error messages

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper) library

## Installation

1. Clone the repository or download the source code files.

2. Install the required dependencies by running the following command:
pip install praw
Copy code
3. Obtain the necessary credentials from Reddit:
- Go to https://www.reddit.com/prefs/apps
- Click on "Create App" or "Create Another App"
- Fill in the required details:
  - Name: Choose a name for your bot
  - App type: Select "Script"
  - Description: Provide a brief description of your bot
  - Redirect URI: Enter "http://localhost:8080"
- Note down the generated client ID and client secret

## Configuration

1. Open the `reddit_comment_detector.py` file in a text editor.

2. Replace the placeholders in the code with your actual credentials:
- `YOUR_CLIENT_ID`: The client ID of your Reddit application
- `YOUR_CLIENT_SECRET`: The client secret of your Reddit application
- `YOUR_REDDIT_USERNAME`: Your Reddit username
- `YOUR_REDDIT_PASSWORD`: Your Reddit password
- `YOUR_BOT_NAME`: A name for your bot (used as the user agent)
- `YOUR_SUBREDDIT_NAME`: The name of the subreddit you want to monitor

3. Customize the `target_phrase` variable with the phrase you want to detect in comments.

4. (Optional) Modify the code inside the `for` loop to perform desired actions when a matching comment is found.

## Usage

1. Run the bot by executing the following command:
python reddit_comment_detector_app.py

2. The bot will start streaming comments from the specified subreddit in real-time.

3. Whenever a comment containing the target phrase is found, the bot will print the permalink of the comment.

4. The bot will continue running until manually interrupted (e.g., by pressing Ctrl+C).

## Disclaimer

Please ensure that you comply with Reddit's API rules and guidelines when using this bot. Respect the terms of service and avoid spamming or engaging in any malicious activities. Use the bot responsibly and at your own risk.

## License

This project is open-source and available under the [MIT License](LICENSE).
Feel free to customize and enhance the README file based on your specific requirements and additional features of your bot.
