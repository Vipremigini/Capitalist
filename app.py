import os
from slack_sdk import WebClient as app
from slack_sdk.errors import SlackApiError 

slack_token = os.environ.get('buoat')


client = app(token=slack_token)

try:
	response = client.chat_postMessage(
    				channel="C07F7MP99MH",
    				text="Bot's first message")
	
	
except SlackApiError as e:
	assert e.response["error"]
	
