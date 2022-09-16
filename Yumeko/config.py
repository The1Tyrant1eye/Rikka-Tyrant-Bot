# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/yumeko/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 8477975  # integer value, dont use "6973446"
    API_HASH = "c093e068dc7c42309ccc2de125b6c1b3"
    TOKEN = "5278580353:AAFXFnQ-cfhdeUB-U0oUkgpiyqa9TUjApRU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "1635151800"  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Sneha_UwU_OwO"
    SUPPORT_CHAT = "tyranteyeeee"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001546153360
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001546153360
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "sqldbtype://username:pw@hostname:port/db_name"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "29sw~FuIbphLGXWd38AYb6VnlJ86DKKfnjWHS91VlpUUSyzpHoVlZWxQ0F4P_ZTy"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "5086893460" "5069705982" "510724476" "1883976677" "5145883564" "1606167442"  "5597384270 "1471781417" "5341414058" "1974783265")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "5086893460" "5372700643" "5380679553" "5544740697" "5598826878" "5589066429" "5282198056" "949365920 ")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "2071450384" "5313362410" "5395870942" 
"2039336161" "5153636966" "5213143273" "5555455171")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "5200936808")
    WOLVES = get_user_list("elevated_users.json", "1963422158")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "V7NS1NBFEL4X24L6"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "2AS711XS1O9B"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
