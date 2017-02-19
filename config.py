from jsonrpc2 import JsonRpc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from os import getenv

cfg = yaml.load(open('config.yml'))

prefix = "TIME_TABLE"

hostname = cfg["pg"]["host"]
hostname = getenv(f"{prefix}_PG_HOST", hostname)
username = cfg["pg"]["username"]
username = getenv(f"{prefix}_PG_USERNAME", username)
dbname = cfg["pg"]["db"]
dbname = getenv(f"{prefix}_PG_DB", dbname)

rpc = JsonRpc()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}@{hostname}/{dbname}"
db = SQLAlchemy(app)

SECRET = cfg["secret"]
SECRET = getenv(f"{prefix}_SECRET", SECRET)
PORT = cfg["http"]["port"]
PORT = getenv(f"{prefix}_HTTP_PORT", PORT)
