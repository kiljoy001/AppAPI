from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/api/public')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/private')
def helper():
    return helper


@app.route('/api/private/user')
def user():
    return user


@app.route('/api/private/user/login')
def login():
    return login


if __name__ == '__main__':
    app.run()
