from flask import Flask, request
import random
import psycopg2
import os

con = psycopg2.connect(database="verceldb", user='default', password=os.environ['POSTGRES_PASSWORD'], host=os.environ["POSTGRES_HOST"])

cur = con.cursor()

f = open("facts.txt","r")
lines = f.readlines()

app = Flask(__name__)

@app.post("/api/try")
def trial():
    leng = len(lines)
    randnum = random.randint(0, leng)
    fact = lines[randnum]
    cur.execute("insert into try values(763);")
    con.commit()
    cur.execute("select * from try")
    data = cur.fetchall()
    data = str(data)
    
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": data
      }
    }]}
