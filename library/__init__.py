from flask import Flask

print("__init__ called")
__version__ = '0.1.0'
app = Flask(__name__)

from library import routes

