import discord
from discord.ext import commands
from replit import db
import stayin_alive

TOKEN = db["token"]
bot = discord.Client()
bot = commands.Bot(command_prefix="-")

# When the bot is ready for use
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord?')
  
# Commands should be written between the dotted lines
#-----------------------

# Example commands
# In discord enter the command prefix + function name
  # Ex. -speak
# Help function is built in for this bot style, but individual messages such as
  # command descriptions still need to be manually set as below
@bot.command(help = 'Prints "Hey Kiddo" to the chat')
async def speak(ctx):
  await ctx.channel.send("Hey Kiddo")


#_______________________  
# Keep at end of file
stayin_alive.stayin_alive()
bot.run(TOKEN)