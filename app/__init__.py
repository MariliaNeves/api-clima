# -*- encoding: utf-8 -*-
from flask import Flask
from .config import Config

app = Flask(__name__)

# load Configuration
app.config.from_object(Config)

from app import views
