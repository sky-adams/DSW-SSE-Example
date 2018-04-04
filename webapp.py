from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/hello')
def publish_hello():
  sse.publish({"message": "Hello!"}, type='greeting')
  return "Message sent!" #where does this go?

if __name__ == '__main__':
    app.run()
