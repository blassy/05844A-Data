
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "Hello, %s" % username

@app.route('/profile/<int:post_id>')
def post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

if __name__=="__main__":
    app.run(debug=True)
    
    