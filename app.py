from flask import Flask, request
import random
import psycopg2
import os

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
        return {"blocks": [
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
                    "text": str(data)
                }
            }]}
        


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
