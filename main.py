#Discord-Related

import discord 
from keep_alive import keep_alive
from discord import Intents
from discord.ext import commands
from discord import app_commands

#Command-Related/Other

from lists import name_list, title_list,spamton
from urllib.request import urlopen
from random import randint,choice
import logging
import os
from dotenv import loaddotenv


#Bots Version
version ='1.5'


#Logging Setup
logging.basicConfig (

  filename='devlogs.txt', 

  level=logging.DEBUG,

  format="%(asctime)s %(message)s\n\n"

)

#Other setup
author_id = 928109349140824125
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#Username Command
@tree.command(name = "username8", description = "Generate a random Username")
async def username8(interaction):
    z = randint(0,len(name_list) - 1) 
    za = randint(0, len(title_list) - 1)
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    wordlist = html.split('\n')
    name = []
    randomnumero = randint(0,4)
    if randomnumero == 0:
     name.append(wordlist[randint(1, len(wordlist) - 1)])
     name.append(wordlist[randint(1, len(wordlist) - 1)])
     print('0')
    elif randomnumero == 1:
        name.append(str(name_list[z]))
        name.append(wordlist[randint(1, len(wordlist) - 1)])
        print('1')
    elif randomnumero == 2:
        name.append(wordlist[randint(1, len(wordlist) - 1)])
        name.append(str(name_list[z]))
        print('2')
    elif randomnumero == 3:
        name.append(str(name_list[z]))  
        name.append(str(title_list[za]))
        print('')
    elif randomnumero == 4:
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
    await interaction.response.send_message(usernamec)

  
#roblox command

  
@tree.command(name = "robloxuser", description = "Generate a random roblox user")
@app_commands.describe(minid='Minimum ID for search', maxid='Maximum ID for search')
async def Roblox_User(interaction: discord.Interaction, minid: app_commands.Range[int, 0, 10000000000], maxid: app_commands.Range[int, 0, 10000000000]):
    loop = 0
    min = int(minid)
    max = int(maxid)
    await interaction.response.defer()
    userID = randint(int(min), int(max))
    weblink = "https://web.roblox.com/users/" + str(userID) + "/profile"
    url = weblink
    while loop < 100:
      try:
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        unformatted = html.split('username":"')[1]
        formatted = unformatted.split('"')[0]
        loop = 1000
        print('yea ok')
      except:
        loop += 1
        if loop == 100:
          formatted = ("N/A")

    
    await interaction.followup.send('User ID: '+str(userID)+'\nUserName: '+formatted)

@tree.command(name='reportissue' , description='Report an Issue')
@app_commands.describe(issue='The Issue to report')
async def reportissue(interaction: discord.Interaction, issue: str):
  await interaction.response.defer()
  author = str(interaction.user.id)
  report_file = open('reports.txt','a')
  report_file.writelines(author+' in verison: '+version+' Sent Issue:\n'+issue +'\n\n\n')
  await interaction.followup.send("Your issue has been logged! Thanks for helping Ubot grow!")

@tree.command(name='big_shot',description='i cant use caps im [[sad]]')
async def bigshot(interaction: discord.Interaction):
  await interaction.response.send_message(choice(spamton))


@tree.command(name='pogcheck',description='bor is  p tpg vbfebgy' )
async def pogcheck(interaction: discord.Interaction):
  await interaction.response.send_message('You are '+randint(0,100)+'% pog')

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")
    logging.info(("Ready!"))



keep_alive()  
token = (loaddotenv("token.env")) 
client.run(token)