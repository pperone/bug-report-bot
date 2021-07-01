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
    # debug = "{'type': 'message', 'subtype': 'bot_message', 'text': '6/30/2021 17:18:27\n\n*Reporter:*\ntest\n<mailto:test@test.com|test@test.com>\n\n*Area:*\nBossSite\n\n*Summary of Issue:*\ntest\n\n*How to Reproduce:*\n\n\n*URL:*\n\n\n*User ID(s):*\n\n\n*Transaction ID(s):*\n\n\n*Vehicle ID(s):*\n\n\n*Screenshots:*\n\n\n\n\n\n*Severity?*\nPERFORMANCE ISSUE - Application is taking too long to perform\n', 'suppress_notification': False, 'username': 'BugBot', 'icons': {'emoji': ':bug:', 'image_64': 'https://a.slack-edge.com/production-standard-emoji-assets/13.0/apple-large/1f41b.png'}, 'bot_id': 'B0VCNJ3QR', 'team': 'T02FPTL8D', 'bot_profile': {'id': 'B0VCNJ3QR', 'deleted': False, 'name': 'Zapier', 'updated': 1587492924, 'app_id': 'A024R9PQM', 'icons': {'image_36': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-06-20/200850512066_2d5e268a3b71c87f969c_36.png', 'image_48': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-06-20/200850512066_2d5e268a3b71c87f969c_48.png', 'image_72': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-06-20/200850512066_2d5e268a3b71c87f969c_72.png'}, 'team_id': 'T02FPTL8D'}, 'source_team': 'T02FPTL8D', 'user_team': 'T02FPTL8D', 'channel': 'C0SLYBWQZ', 'event_ts': '1625091664.320700', 'ts': '1625091664.320700'}"
    print(event)

    if event["type"] == "message":
        if event["subtype"] == "bot_message":
            pass
        else:
            client.web_client.chat_postMessage(
                channel = CHANNEL,
                text = ":warning: *Reminder:* if you'd like to report a bug, please fill out *<https://goo.gl/forms/yLWoLKdMDHdfLmkf2|this form>* and add as much information as possible. Thank you!"
            )


# Initializer
rtm.start()