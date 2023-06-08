import PIL
import os
import textwrap
import requests
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

#getting the API Quote
api = "http://api.quotable.io/random"
quoteJson = requests.get(api).json()
content = quoteJson["content"]
author = quoteJson["author"]
brContent = content.replace('\n',' [br] ')
splitCont = content.split()

#Wrapping the text of the quote
#wrapCont = textwrap.wrap(content,width=10)

#Getting the file path of the font
dirname = os.path.dirname(__file__)
fontFileName = os.path.join(dirname, 'Fonts/font_1.ttf')
font = ImageFont.truetype(fontFileName,175)
subTextFont = ImageFont.truetype(fontFileName,100)

#Load the image & get its length and width
bgFileName = os.path.join(dirname, 'Background_Images/bg_1.jpg')
image = Image.open(bgFileName)
x,y = image.size

#print("width: ",str(x)," height: ",str(y))

#Prep Image for the drawing
drawing = ImageDraw.Draw(image)

#Get the quote and and insert the text

#Problem: How will I make the text wrap automatically?
#Potential solution, count the number of characters and if they're over a certain number, wrap the text.
#Might need to implement a loop that will itterate and keep adding the remaining characters until finished
xLeftMargin = round(x * .1)
xRightMargin = round(x * .9)

xCoordQuote = xLeftMargin
yCoordQuote = round(y * 1/10)
offsetQuote = 10

#Create coordinates for the quote at the bottom
xCoordBrand = xLeftMargin * 3.6
yCoordBrand = yCoordQuote * 9.1  
offsetBrand= offsetQuote - 2

space = 0
enter = 0

spaceVar = 50

#Branding
drawing.text((xCoordBrand,yCoordBrand),"Persistance X Passion",(0,0,0),font=subTextFont)
drawing.text((xCoordBrand-offsetBrand,yCoordBrand-offsetBrand),"Persistance X Passion",(255,255,255),font=subTextFont)

#Quote Loop
current = 0
charTotal = xLeftMargin
while (current < len(splitCont)):
    
    drawing.text((xCoordQuote+space,yCoordQuote+enter),splitCont[current],(0,0,0),font=font)
    drawing.text(((xCoordQuote+space)-offsetQuote,(yCoordQuote+enter)-offsetQuote),splitCont[current],(255,255,255),font=font)
 

    space += font.getsize(splitCont[current])[0] + spaceVar
    charTotal = charTotal + font.getsize(splitCont[current])[0] + spaceVar
   
    
    #you need to keep track of the number of characters that have been placed and use that length to check if the future word will break that
    if current + 1 < len(splitCont) and charTotal + font.getsize(splitCont[current+1])[0] + spaceVar >= xRightMargin:
        #reset line total
        charTotal = xLeftMargin
        #New Lines
        yCoordQuote += 200
        #Reset space
        space = 0
    
    current += 1

#Author
authorH = "-"+author
drawing.text((xLeftMargin,yCoordQuote+200),authorH,(0,0,0),font=subTextFont)
drawing.text((xLeftMargin-offsetBrand,(yCoordQuote+200)-offsetBrand),authorH,(255,255,255),font=subTextFont)



image.show()

#Save Image
#testImg.save("a_test.png")