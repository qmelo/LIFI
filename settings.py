import os

from dotenv import load_dotenv

load_dotenv()

MASTER_GUILD_ID = int(os.environ['MASTER_GUILD_ID'])

DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']

DATABASE_URL = os.environ['DATABASE_URL']
