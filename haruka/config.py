if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "854898207:AAEApr0vNNQJ3Ib9ulUzDVcbkqJMXM5dMZc"
    OWNER_ID = "765989818"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "spider_binner"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # needed for any database modules
    MESSAGE_DUMP = '-1234567890' # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = ANYTHING
    URL = "https://spiderbins1.herokuapp.com/"

    # OPTIONAL
    SUDO_USERS = [765989818]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [765989818]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [765989818]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADBQADDQADjR\_yKCDDBtuwTt59Ag'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = '' # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
