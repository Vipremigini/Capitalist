from flask import Flask, request
import random
import psycopg2
import os
import requests

con = psycopg2.connect(database="verceldb", user='default', password=os.environ['POSTGRES_PASSWORD'], host=os.environ["POSTGRES_HOST"])

cur = con.cursor()


app = Flask(__name__)

@app.post("/api/register")
def register():
    uid = request.form.get("user_id")
    comm = "select uid from userdata where uid = '" + uid + "'"
    cur.execute(str(comm))
    data = cur.fetchall()
    if data == []:
        comm = "insert into userdata values('" + uid + "' , 500);"
        cur.execute(comm)
        con.commit()
        return { "response_type": "in_channel",
                "blocks": [
            {
                "type": "section",
                "response_type": "in_channel",
                "text": {
                    "type": "mrkdwn",
                    "text": "Registered successfully!! You now have 500 hack dollars"
                }
            }]}
    else:
        return { "response_type": "in_channel",
                "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "You are already registered"
                }
            }]}
        
@app.post("/api/interact")
def reply():
    purl = "https://slack.com/api/chat.postMessage"
    data = request.form
    data = str(data)
    
    obj = {"channel": "C07F7MP99MH","text": data}
    x = requests.post(url,Authorization = os.environ['buoat'],  json = obj)


@app.post("/api/buy")
def buy():
    return { "response_type": "in_channel",
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "hi",
				"emoji": true
			}
		}
	]
}



