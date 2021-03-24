# keys de configuracion se cargan desde un envvars
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEY_YOUTUBE = config('KEY_YOUTUBE')