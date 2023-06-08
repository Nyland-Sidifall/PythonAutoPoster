import time
import random
import os
from pprint import pprint
from instabot import Bot


bot = Bot()
uname = 'Your Username'
pword = 'Your Password'
bot.login(username = uname,password=pword)

medias = bot.get_total_user_medias(bot.user_id)

print(medias)

try:
    print("Last post was ",str(medias[0]))
except:
    print("error")

