from flask import Flask

# app
app = Flask(__name__)

from routes.index import *

if __name__ == '__main__':

    app.run(debug=True, host='localhost', port=5000)
