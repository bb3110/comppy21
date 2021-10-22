from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello world</h1>"


@app.route('/bye')
def bye():
    return "<h1>Goodbye</h1>"


app.run()
