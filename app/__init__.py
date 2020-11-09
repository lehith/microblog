from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# login.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу."
mail = Mail(app)
bootstrap = Bootstrap(app)


from app import routes, models, errors, logger
