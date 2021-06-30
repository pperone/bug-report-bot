import os
import time
import re

from slack import WebClient


# Turn this to true for full messages to be sent to debugging Slack channel
debugging = False
debug_channel = 'C027DKQ9P5W'

# Slack setup
slack_client = WebClient(os.environ.get('BRBOT_TOKEN'))
brbot_id = None

# Constants
CHANNEL = 'G0E437QDD'
RTM_READ_DELAY = 1


# Processes the message
def parse_bot_commands(slack_events):
    # ev = {"type": "message", "subtype": "bot_message", "text": "", "suppress_notification": False, "username": "Slackistrano", "icons": {"image_48": "https://s3-us-west-2.amazonaws.com/slack-files2/bot_icons/2017-05-24/187498878213_48.png"}, "bot_id": "B0E14A2BA", "team": "T02FPTL8D", "bot_profile": {"id": "B0E14A2BA", "deleted": False, "name": "incoming-webhook", "updated": 1446819626, "app_id": "A0F7XDUAZ", "icons": {"image_36": "https://a.slack-edge.com/80588/img/services/outgoing-webhook_36.png", "image_48": "https://a.slack-edge.com/80588/img/services/outgoing-webhook_48.png", "image_72": "https://a.slack-edge.com/80588/img/services/outgoing-webhook_72.png"}, "team_id": "T02FPTL8D"}, "attachments": [{"fallback": "Pablo Ulguin has finished deploying branch master of backlotcars to production", "title": "New version deployed :boom::bangbang:", "id": 1, "color": "2eb886", "fields": [{"title": "Environment", "value": "load-test", "short": True}, {"title": "Branch", "value": "master", "short": True}, {"title": "Deployer", "value": "Pablo Ulguin", "short": True}, {"title": "Revision", "value": "53b853d", "short": True}, {"title": "Time to deploy", "value": "04:37", "short": True}, {"title": "www", "value": "https://backlotcars.com", "short": True}]}], "channel": "G0E437QDD", "event_ts": "1589220562.071000", "ts": "1589220562.071000"}

    for event in slack_events:
        if 'channel' in event:
            if event["channel"] == debug_channel: 
                if event["type"] == "message":
                    handle_event(event)
                    # if "attachments" in event:
                    #     if "title" in event["attachments"][0]:
                    #         handle_event(org, event)
                
                # handle_event(org, ev)

                # slack_client.api_call(
                #     "chat.postMessage",
                #     channel = debug_channel,
                #     text = event,
                #     as_user = True
                # )
                # session.commit()
                    
    return None, None

def handle_event(event):
    response = "Hey"

    slack_client.api_call(
        "chat.postMessage",
        channel = debug_channel,
        text = response,
        as_user = True
    )
    session.commit()

    # if not production:
    #     if debugging:
    #         slack_client.api_call(
    #             "chat.postMessage",
    #             channel = debug_channel,
    #             text = response,
    #             as_user = True
    #         )
    #         session.commit()
    #     else:
    #         slack_client.api_call(
    #             "chat.postMessage",
    #             channel = CHANNEL,
    #             text = response,
    #             as_user = True
    #         )
    #         session.commit()


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Bug Report Bug connected")
        brbot_id = slack_client.api_call("auth.test")["user_id"]

        while True:
            parse_bot_commands(slack_client.read())
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
