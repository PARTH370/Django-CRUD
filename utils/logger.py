import os
import json
from loguru import logger as app_logger
from pathlib import Path
import platform
import os

from decouple import config
baseDir = Path(__file__).resolve().parent.parent
_info_log_dir = os.path.join(baseDir,"logs")
_info_log_dir_trace = os.path.join(baseDir,"logs")
directory_path = os.getcwd()
directory_path = directory_path + "\logs"


# def get_email_config():
#     return ConnectionConfig(
#         MAIL_USERNAME=CONFIG["EMAIL_HOST_USER"],
#         MAIL_PASSWORD=CONFIG["EMAIL_HOST_PASSWORD"],
#         MAIL_FROM=CONFIG["DEFAULT_FROM"],
#         MAIL_FROM_NAME="DPA Cloud Solutions",
#         TEMPLATE_FOLDER="./templates",
#         MAIL_PORT=CONFIG["EMAIL_PORT"],
#         MAIL_SERVER=CONFIG["EMAIL_HOST"],
#         MAIL_TLS=True,
#         MAIL_SSL=False,
#         USE_CREDENTIALS=True,
#         VALIDATE_CERTS=True,
#     )


class Settings():
    SECRET_KEY = config('RTA_CRED_SECRETE_KEY')
    VERSION: str = config('VERSION') 
    SERVICE: str = "form"
    SERVICE_NAME: str = "form"
    API_ENV: str = config('ENV')  # dev/uat/beta/prod
    # API_V1_STR: str = "/api/v1"
    API_INSTANCE: str = config('ENV') + "/" + config('INSTANCE_ID')
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    # CORS_DOMAIN: str = CONFIG["CORS_DOMAIN"]
    # Directory settings
    LOG_DIR: str = os.path.join(os.path.abspath(os.sep), directory_path)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    # Email
    # EMAIL_SETTINGS: ConnectionConfig = get_email_config()
    OTP_EXPIRY_TIME = 300
    VERIFICATION_EXPIRY_TIME = 64800
    # My-SQL
    # SQLALCHEMY_DATABASE_URL: str = CONFIG["MYSQL_URI"]
    #
    GENERAL_HTTP_400: dict = {
        401: {
            "content": {
                "application/json": {"example": {"detail": "Not Authenticated"}}
            }
        },
        403: {
            "content": {"application/json": {"example": {"detail": "Not Authorized"}}}
        },
        404: {"content": {"application/json": {"example": {"detail": "Not Found"}}}},
    }
    LOG_FORMAT: str = (
        "{time: YYYY-MM-DD HH:mm:ss.SSS} | "
        + SERVICE
        + " | "
        + API_INSTANCE
        + " | {level} | {function} | {message}"
    )

    class Config:
        case_sensitive = True
API_INSTANCE: str = config('ENV') + "/" + config('INSTANCE_ID')
LOG_FORMAT: str = (
        "{time: YYYY-MM-DD HH:mm:ss.SSS} | "
        + "form"
        + " | "
        + API_INSTANCE
        + " | {level} | {function} | {message}"
    )


app_logger.configure(
    handlers=[
        {
            "sink": os.path.join(_info_log_dir, "info.log"),
            "level": "DEBUG",
            "colorize": False,
            "format": LOG_FORMAT,
            "rotation": "00:00",
            "compression": "zip",
        },
        {
            "sink": os.path.join(_info_log_dir_trace, "trace.log"),
            "level": "TRACE",
            "colorize": False,
            "format": LOG_FORMAT,
            "rotation": "10MB",
            "compression": "zip",
        },
    ]
)
