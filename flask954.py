from flask import Flask, jsonify
app = Flask(__name__)
from tweeter1149 import tweeterTimeline
url='192.168.0.21'
port = 5050
'''
tweeter account : faridi56888245

'''
@app.route('/')
def hello_world():
   return "Success"


@app.route('/tweeter/')
def timeline():
   lt = tweeterTimeline.tweet_timeline("realDonaldTrump", 5)
   return jsonify(lt)


if __name__ == '__main__':
   app.run(host=url,port=port)