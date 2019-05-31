# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from config import Config



app = Flask(__name__) # create the application instance :)
app.config.from_object(Config) # load config from this file , flaskr.py

app.config.from_envvar('MAIN_SETTINGS', silent=True)
#from main import routes  