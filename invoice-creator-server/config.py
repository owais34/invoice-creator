# config.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save memory
