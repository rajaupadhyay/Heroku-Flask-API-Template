from flask import Flask
from main.config import configure_app

app = Flask(__name__, instance_relative_config=True)
configure_app(app)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

import main.models
import main.views