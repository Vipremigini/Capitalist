import os
from flask import Flask, request
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler
app = Flask(__name__)
bolt_app = App(token=os.environ.get('buoat'), signing_secret=os.environ.get('sss'))
handler = SlackRequestHandler(bolt_app)


@app.route("/api/events", methods=["POST"])
def slack_events():
 
    return handler.handle(request)

@bolt_app.message("hello slacky")
def greetings(payload: dict, say: Say):
   
    user = payload.get("user")
    say(f"Hi <@{user}>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
