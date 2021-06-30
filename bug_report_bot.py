import os
import time
import re

from slack_sdk.rtm_v2 import RTMClient


# Turn this to true for full messages to be sent to debugging Slack channel
debugging = False
debug_channel = 'C027DKQ9P5W'

# Slack setup
rtm = RTMClient(token=os.environ["BRBOT_TOKEN"])

# Constants
CHANNEL = 'C0SLYBWQZ'
RTM_READ_DELAY = 1


# Processes the message
@rtm.on("message")
def handle(client: RTMClient, event: dict):
    if event["type"] == "message":
        if "attachments" in event:
            print(event)
            client.web_client.chat_postMessage(
                channel = debug_channel,
                text = ":burger: Nothingburger"
            )
        else:
            client.web_client.chat_postMessage(
                channel = debug_channel,
                text = ":warning: *Reminder:* if you'd like to report a bug, please fill out *<https://goo.gl/forms/yLWoLKdMDHdfLmkf2|this form>* and add as much information as possible. Thank you!"
            )


# Initializer
rtm.start()