## Example code to getting started
## with flask application

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello there!"

if __name__ == '__main__':
    app.run(debug=True)
