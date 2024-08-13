import os
from flask import Flask, request
from slack_bolt import App, Say
from slack_bolt.adapter.flask import SlackRequestHandler
app = Flask(__name__)
bolt_app = App(token="hi", signing_secret="hi"))
handler = SlackRequestHandler(bolt_app)


@app.route("/api/events", methods=["POST"])
def slack_events():
    """ Declaring the route where slack will post a request """
    return handler.handle(request)

@bolt_app.message("hello slacky")
def greetings(payload: dict, say: Say):
    """ This will check all the message and pass only those which has 'hello slacky' in it """
    user = payload.get("user")
    say(f"Hi <@{user}>")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
