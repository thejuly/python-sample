from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<user>')
def profile(user):
    return '<h2>Tuna is good %s</h2>' % user

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2>Tuna is good %s</h2>' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
