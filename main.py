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
  



#_______________________  
# Keep at end of file
stayin_alive.stayin_alive()
bot.run(TOKEN)