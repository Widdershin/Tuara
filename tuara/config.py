import os

SECRET_KEY = str(os.getenv("TUARA_SECRET_KEY"))
MONGODB_SETTINGS = {"DB": "tuara"}