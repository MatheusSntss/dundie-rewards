import os

SMTP_HOST = "localhost"
SMTP_PORT = 8025
SMTP_TIMEOUT = 5

EMAIL_FROM = "master@dundie.com"

FILE_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(FILE_PATH, "..", "assets", "database.json")
