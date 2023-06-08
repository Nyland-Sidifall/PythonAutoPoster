import time
import random
import os
from pprint import pprint
from instabot import Bot

uname = 'Your Username'
pword = 'Your Password'

#Delete UUID
os.chdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/config/") 
os.remove(uname+"_uuid_and_cookie.json")
os.chdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/auto_poster_chron") 

img_id = 'empty str'

bot = Bot()
bot.login(username = uname,password=pword)

medias = bot.get_total_user_medias(bot.user_id)

myfile = open("image_id.txt","r")
img_id = myfile.readline()
print('old ig id:', str(img_id))
myfile.close()

try:
    if img_id in medias:
        print('Image Found: ',img_id,' will be deleted.')
        bot.delete_media(img_id)
    else:
        print('Image Id Not Found!')
    
except:
    print('Error with accessing IG')

