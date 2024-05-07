pip install praw
import praw
import time

# Replace the placeholders with your actual credentials
client_id = "YourID"
client_secret = "YourSecret"
username = "YourRedditUsername"
password = "YourRedditPassword"
user_agent = "YourBotsName"

# Create a Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Specify the subreddit to monitor
subreddit_name = "OpenAI"
subreddit = reddit.subreddit(subreddit_name)

# Phrase to detect
target_phrase = "I am a business owner interested in AI"

# Stream comments in real-time
try:
    for comment in subreddit.stream.comments():
        if target_phrase.lower() in comment.body.lower():
            print(f"Found comment: {comment.permalink}")
            # Perform desired actions here, such as replying to the comment

        time.sleep(1)  # Add a delay to avoid hitting rate limits

except praw.exceptions.ResponseException as e:
    print(f"Authentication failed. Please check your credentials. Error: {e}")
