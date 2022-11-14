import os

from slack_sdk.rtm_v2 import RTMClient


# Turn this to true for full messages to be sent to debugging Slack channel
debugging = False
DEBUG_CHANNEL = 'C027DKQ9P5W'

# Slack setup
rtm = RTMClient(token=os.environ["BRBOT_TOKEN"])

# Constants
CHANNEL = 'C0SLYBWQZ'
RTM_READ_DELAY = 1


# Processes the message
@rtm.on("message")
def handle(client: RTMClient, event: dict):
    mention = "<@" + event["user"] + ">"

    if event["channel"] == CHANNEL:
        if event["type"] == "message":
            if "subtype" in event:
                pass
            elif "thread_ts" in event:
                pass
            elif "message" in event:
                if "thread_ts" in event["message"]:
                    pass
            else:
                client.web_client.chat_postMessage(
                    channel = CHANNEL,
                    thread_ts = event["ts"],
                    text = "%s: if you'd like to report a bug, please fill out the form at *<https://goo.gl/forms/yLWoLKdMDHdfLmkf2|https://goo.gl/forms/yLWoLKdMDHdfLmkf2>* and add as much information as possible. Thank you!" %(mention)
                )


# Initializer
rtm.start()
