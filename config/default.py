import os


DEBUG = False


DB_USER = os.environ.get("MGI_DB_USER", "mgincident_app")
DB_PASSWORD = os.environ.get("MGI_DB_PASSWORD")
DB_HOST = os.environ.get("MGI_DB_HOST", "localhost")
DB_NAME = os.environ.get("MGI_DB_NAME", "mgincident")


SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
)
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECURITY_URL_PREFIX = ""
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "KJbGHUIFklaihHOIH809HGbldSsj8"

SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/"
SECURITY_POST_LOGOUT_VIEW = "/"
SECURITY_POST_REGISTER_VIEW = "/"

SECURITY_REGISTERABLE = False
SECURITY_SEND_REGISTER_EMAIL = False
