import os

from flask.cli import load_dotenv
from twilio import rest
from twilio.rest import Client
from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
from twilio import twiml

load_dotenv()
import requests
from bs4 import BeautifulSoup

# run with python3.app.py
app = Flask(__name__)
my_request_client = rest

client = Client(os.getenv("AC9b30eb6d8d8cfdd530e4842845154337"), os.getenv("c170c69b1727a7f80a214bb513215391"),
                http_client=my_request_client)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    resp = twiml.Response()
    resp.message('Hello from BostonHacks'.format(number, message_body))
    return str(resp)


# with open("index.html") as fp:
#     soup = BeautifulSoup(fp)
#
# soup = BeautifulSoup("<html>data</html>")
# import urllib
#
# # Account SID and Auth Token from www.twilio.com/console
# client = Client('AC9b30eb6d8d8cfdd530e4842845154337', 'c170c69b1727a7f80a214bb513215391')

#
#
# # A route to respond to SMS messages and kick off a phone call.
# @app.route('/sms', methods=['POST'])
# def inbound_sms():
#     response = MessagingResponse()
#     response.message('Hello from BostonHacks')
#     from_number = request.form['From']
#     to_number = request.form['To']
#     client.api.account.messages.create(body= 'Hello from BostonHacks', to=from_number, from_=to_number)
#     print(response)
#     return str(response)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
