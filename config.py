import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28406888"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ec9254428ab2a6a5332c80f0ce9108a0")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7400528362"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ajayyadaw991:koNs1csE7KFqHxaZ@cluster0.rfkucjw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
