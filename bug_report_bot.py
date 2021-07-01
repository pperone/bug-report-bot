import os

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
        if event["subtype"] == "bot_message":
            pass
        elif event["subtype"] == "message_replied":
            pass
        elif "thread_ts" in event:
            pass
        elif event["subtype"] == "message_deleted":
            pass
        else:
            client.web_client.chat_postMessage(
                channel = CHANNEL,
                text = ":warning: *Reminder:* if you'd like to report a bug, please fill out *<https://goo.gl/forms/yLWoLKdMDHdfLmkf2|this form>* and add as much information as possible. Thank you!"
            )
    
    client.web_client.chat_postMessage(
        channel = debug_channel,
        text = event
    )


# Initializer
rtm.start()
