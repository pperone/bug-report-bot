import os
import logging

from slack_bolt import App

# Initializes your app with your bot token and signing secret
logging.basicConfig(level=logging.DEBUG)

app = App(
    token=os.environ.get("BRBOT_TOKEN"),
    signing_secret=os.environ.get("BRBOT_SECRET")
)

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    logger
    say(f"Hey there <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))