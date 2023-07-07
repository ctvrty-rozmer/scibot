# bot.py

# allows us to import shit
import os
# import discord api shit
import discord
# allows us to create discord commands
from discord.ext import commands
# allows us to load environment variables from separate .env file
from dotenv import load_dotenv
from scihub import SciHub






#loads information from .env, in this case its DISCORD_TOKEN
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# weird intent shit that discord makes us do now for some reason
intents = discord.Intents.default()
# allows us to view message content ie commands
intents.message_content = True
# sets the command prefix plus weird intents shit
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

#command time baby
@bot.command()
#create ping command
async def ping(ctx):
  #respond to ping command with Pong!
  await ctx.send("Pong!")
#runs the bot using the token from .env file

@bot.command()
async def scifetch(ctx, arg):
  sh = SciHub()

# fetch specific article (don't download to disk)
# this will return a dictionary in the form 
# {'pdf': PDF_DATA,
#  'url': SOURCE_URL,
#  'name': UNIQUE_GENERATED NAME
# }

  result = sh.fetch(arg)
  if "err" in result:
    await ctx.send(result["err"])
  else:
    urldata = (result['url'])
    await ctx.send(urldata)

bot.run(TOKEN)
