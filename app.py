from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World 25!'

@app.route('/api/v1/hello-world-25')
def hello_world_25():
    return 'Hello World 25', 200

if __name__ == '__main__':
    app.run(debug=True)
