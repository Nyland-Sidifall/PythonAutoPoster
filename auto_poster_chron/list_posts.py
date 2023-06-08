import time
import random
import os
from pprint import pprint
from instabot import Bot

#Change directory to uuid location
os.chdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/config/") 

#List & print directory
print(os.path.dirname(os.getcwd()))
dirlist = os.listdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/config/")
pprint(dirlist)

os.remove("m_limitbreak_uuid_and_cookie.json")

#List directory after removing uuid
dirlist = os.listdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/config/")
pprint(dirlist)

#Change directory to autoposter
os.chdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/auto_poster_chron") 

#print directory
print(os.path.dirname(os.getcwd()))

#List directory of chron
dirlist = os.listdir(r"/Users/nylandsidifall/Documents/VSCode_Projects/Python/auto_poster_chron")
pprint(dirlist)

img_id = 'empty str'

"""
#Read in current ig data id
myfile = open("image_id.txt","r")
img_id = myfile.readline()
print('old print: ',str(img_id))
myfile.close()

#write over for new ig id
myfile = open("image_id.txt","w")
myfile.write('New IG ID')
myfile.close()

#print new IG ID for later
myfile = open("image_id.txt","r")
img_id = myfile.readline()
print('new print: ',str(img_id))
myfile.close()
"""

bot = Bot()
uname = 'Your Username'
pword = 'Your Password'
bot.login(username = uname,password=pword)

medias = bot.get_total_user_medias(bot.user_id)

myfile = open("image_id.txt","r")
img_id = myfile.readline()
print('old ig id:', str(img_id))
myfile.close()

try:
    for x in medias:
        if x == img_id:
            print('Image Found, preped for deletion.')
            bot.delete_media(img_id)
            break
    print('Could not find picture')
except:
    print('Error with accessing IG')

