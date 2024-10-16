import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="+")  # The prefix for commands

@bot.event
async def on_ready():
    print(f"Bot is online! Logged in as {bot.user.name}")
    
    # Custom activity for the bot
    activity = discord.Game("with code!")  # You can change this to anything
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run('MTI4NDE4NjUzNzA4MDEyNzU5MQ.GZmc2C._hyP95zPDW5z8SEaLu3OAxTFbYbAVgAvjZpuxc')
