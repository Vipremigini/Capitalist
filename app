from flask import Flask, request
import random

f = open("facts.txt","r")
lines = f.readlines()

app = Flask(__name__)

@app.post("/api/try")
def trial():
    leng = len(lines)
    randnum = random.randint(0, leng)
    fact = lines[randnum]
    
    
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": fact
      }
    }]}
