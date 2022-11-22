import discord
import os
from keep_alive import keep_alive
from discord import client,Intents
from discord.ext import commands
from lists import name_list, title_list,spamton
from urllib.request import urlopen
from random import randint
import logging
intents = discord.Intents.default()
intents.messages = True
version ='1.3'
bot = commands.Bot(
	command_prefix="u!",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
  intents=intents 
)
bot.author_id = 928109349140824125
#Logging Setup
logging.basicConfig (

  filename='devlogs.txt', 

  level=logging.DEBUG,

  format="%(asctime)s %(message)s\n\n"

)




@bot.event 
async def on_ready():  # When the bot is ready
    logging.info(("Bot Ready as "+ str(bot.user)))

@bot.command()
async def commands(ctx):
  await ctx.reply("Commands:\nU!Username: Returns Random Username\nU!pogcheck: Are you [[POG]]? RUN THIS [[DISCORD BOT]] COMMAND TO [[FIND OUT]]\nu!ReportIssue: Reports an Issue\nu!BIGSHOT: DO YOU WANT TO BE A [[SHOT BIG?]]")
@bot.command()
async def username(ctx):
   try:
    z = randint(0,len(name_list) - 1) 
    za = randint(0, len(title_list) - 1)
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    wordlist = html.split('\n')
    name = []
    if randint(0,1) == 1:
     name.append(wordlist[randint(1, len(wordlist) - 1)])
     name.append(wordlist[randint(1, len(wordlist) - 1)])
    else:
      if randint(0,1) == 1:
        name.append(str(name_list[z]))
        name.append(wordlist[randint(1, len(wordlist) - 1)])
      else: 
        if randint(0,1) == 1:
          name.append(wordlist[randint(1, len(wordlist) - 1)])
          name.append(str(name_list[z]))
        else:
          if randint(0,1) == 1:
            name.append(str(name_list[z]))  
            name.append(str(title_list[za]))
          else:
            if randint(0,1) == 1:
              name.append("The_Legend_of")
            else:
              name.append("The_Secret_of")
            name.append(str(name_list[z]))
    print("Generated")
    random = randint(0,5)
    if random == 1:
      usernamec = (name[0] + '_' + name[1] + str(randint(1, 9)))
    elif (random == 2): 
      usernamec = (name[0] + '_' + name[1] + str(randint(10,99)))
    elif (random == 3): 
      usernamec = (name[0] + '_' + name[1] + str(randint(100,999)))
    elif (random == 4): 
      usernamec = (name[0] + '_' + name[1] + str(randint(1000,9999)))
    elif (random == 5): 
      usernamec = (name[0] + '_' + name[1] + str(randint(10000,99999)))
    else:
      usernamec = (name[0] + '_' + name[1])
    await ctx.reply('Username: ' +usernamec , mention_author=True)
   except Exception as e:
     logging.critical(('Command (Username Generator) failed with error '+e))
      

@bot.command()
async def pogcheck(ctx):
  await ctx.reply('Pog level: '+ str(randint(0,100))+'%')
try:
  @bot.command()
  async def reportIssue(ctx,Issue:str = None):
    if Issue == None:
      await ctx.reply("Nope. Atleast Write the Issue.")
    else: 
      author = str(ctx.message.author)
      report_file = open('reports.txt','a')
      report_file.writelines(author+' in verison: '+version+' Sent Issue:\n'+Issue +'\n\n\n')
      await ctx.reply('Issue Logged!')
except:
  logging.debug('Error Encountered during reportIssue')
  
@bot.command()
async def BIGSHOT(ctx):
  await ctx.reply(spamton[randint(0,len(spamton)-1)])


  
extensions = [
	'cogs.devcommands'  # Same name as it would be if you were importing it
]



if __name__ == '__main__':  # Ensures this is the file being ran
  for extension in extensions:
    bot.load_extension(extension)  
keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("token") 
bot.run(token)  # Starts the bot