from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
