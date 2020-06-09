import discord
from discord.ext import commands
from decouple import config

TWITCH_NAME = config("TWITCHNAME")
DISCORD_STATUS_TYPE = config("TYPE")
BOT_TOKEN = config("TOKEN")
ENABLE_STATUS = config("STATUS")
STATUS_TITLE = config("STATUS_TITLE")
BOT_PREFIX = config("BOT_PREFIX")
on_ready_message = ""

bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_connect():
    global on_ready_message
    global cogs
    #
    #   Basic User Configuration
    #
    on_ready_message = f">----[Logged In]----<\n> {bot.user.name}\n> {bot.user.id}\n>-------------------<"
    cogs = [
    "cogs.ping"
    ]
    for cog in cogs:
        bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f"{on_ready_message}")
    if ENABLE_STATUS.upper() == "YES":
        if DISCORD_STATUS_TYPE.upper() == "STREAMING":
            await bot.change_presence(activity=discord.Streaming(name=STATUS_TITLE, url="https://www.twitch.tv/" + TWITCH_NAME))
        if DISCORD_STATUS_TYPE.upper() == "PLAYING":
            await bot.change_presence(activity=discord.Game(STATUS_TITLE))
    else:
        pass

bot.run(BOT_TOKEN)
