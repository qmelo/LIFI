import discord
from discord.ext import commands
from prisma import Prisma

from settings import MASTER_GUILD_ID

extensions = ['cogs.example']

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all(),
            help_command=None,
        )
        self.db = Prisma()
        self.custom_emojis = {}

    async def on_ready(self):
        for extension in extensions:
            await self.load_extension(extension)
        # await self.db.connect()
        await self.load_extension('jishaku')
        await self.tree.sync()
        await self.refresh_custom_emojis()
        
    async def refresh_custom_emojis(self):
        self.custom_emojis = {}
        guild = self.get_guild(MASTER_GUILD_ID)
        for emoji in guild.emojis:
            self.custom_emojis[emoji.name] = emoji
