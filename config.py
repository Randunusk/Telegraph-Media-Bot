import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1893746951:AAG2dQocDoC_H9hWfCsOf3KGdhv6Yg0nVW4")

    APP_ID = int(os.environ.get("APP_ID", "6986644")

    API_HASH = os.environ.get("API_HASH", "86794dd20b421ba420a884ace3575ce6")
