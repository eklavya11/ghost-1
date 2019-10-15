import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

# Get important data from the env file.
OWNER_ID = os.getenv('OWNER_ID')
USER_TOKEN = os.getenv('USER_TOKEN')
PREFIX = os.getenv('PREFIX')

# Create a new bot with settings from .env
client = commands.Bot(command_prefix=PREFIX, help_command=None,
                      description=None, self_bot=True, owner_id=OWNER_ID)


# Runs when the on_ready client event is sent
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.command()
async def test(ctx):
    await ctx.send('hey there!')

# Run selfbot
client.run(USER_TOKEN, bot=False)