
import os
from keep_alive import keep_alive
from discord import client,Intents
from discord.ext import commands
from lists import name_list, title_list
from urllib.request import urlopen
from random import randint
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
	command_prefix="u!",  # Change to desired prefix
	case_insensitive=True,  # Commands aren't case-sensitive
  intents=intents 
)

bot.author_id = 928109349140824125  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def username(ctx):
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

  
extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]



if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("token") 
bot.run(token)  # Starts the bot

  
extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]



if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot