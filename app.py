import os
#from flask import Flask



from flask import Flask, request
import json
#import requests


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/thongpoon')
def thongpoon():
    return '<h2>Thongpoon is good</h2>'

@app.route('/profile/<user>')
def profile(user):
    return '<h2>Tuna is good %s</h2>' % user

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2>Tuna is good %s</h2>' % post_id

###############################
@app.route('/callback', methods=['POST'])
def callback():
    a = 123
    '''
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded["events"][0]['replyToken']
    #id=[d['replyToken'] for d in user][0]
    #print(json_line)
    print("ผู้ใช้：",user)
    sendText(user,'งง') # ส่งข้อความ งง
    return '',200
    '''
##############################



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
