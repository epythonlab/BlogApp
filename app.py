from flask import Flask
from db import db
# app
app = Flask(__name__)

# create configuration and initialize plugins
app.config.from_object("config.Config")

db.init_app(app)

from routes.index import *

with app.app_context():
    # create if database not exist'sc
    db.create_all()

if __name__ == '__main__':

    app.run(debug=True, host='localhost', port=5000)
