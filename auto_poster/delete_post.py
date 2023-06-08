import time
import random
from instabot import Bot

bot = Bot()
uname = 'Your Username'
pword = 'Your Password'
bot.login(username = uname,password=pword)

medias = bot.get_total_user_medias(bot.user_id)

print(medias)

try:
    bot.delete_media(medias[0])
    print("Done Deleting Pic")
except:
    print("error")

