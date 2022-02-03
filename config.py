# Configuration, just like it says on the cover
# config.py
import os

class Config(object):

    SECRET_KEY = os.urandom(32)
    # Grabs the folder where the script runs.
    basedir = os.path.abspath(os.path.dirname(__file__))
    # Enable debug mode.
    DEBUG = True
    # Connect to the database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1838/02@localhost/blogapp'

    # Turn off the Flask-SQLAlchemy event system and warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_PASSWORD_SALT =""

    UPLOAD_FOLDER = '/static/uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
