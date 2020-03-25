from dot-env import load_dotenv
import os


load_dotenv()

class Config:
    """ Base configuration reading from .env file """
    DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get("SECRET_KEY")