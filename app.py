from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!"


@app.route('/greet/<name>', methods=["GET"])
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
