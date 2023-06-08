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
#print("The len of string: ",len(content)," content: ",content)


#Wrapping the text of the quote
wrapCont = textwrap.wrap(content,width=10)

#Getting the file path of the font
dirname = os.path.dirname(__file__)
fontFileName = os.path.join(dirname, 'Fonts/font_1.ttf')
font = ImageFont.truetype(fontFileName,175)
subTextFont = ImageFont.truetype(fontFileName,100)

#Load the image & get its length and width
bgFileName = os.path.join(dirname, 'Background_Images/bg_1.jpg')
image = Image.open(bgFileName)
x,y = image.size

print("width: ",str(x)," height: ",str(y))

#Prep Image for the drawing
drawing = ImageDraw.Draw(image)

#Get the quote and and insert the text

#Problem: How will I make the text wrap automatically?
#Potential solution, count the number of characters and if they're over a certain number, wrap the text.
#Might need to implement a loop that will itterate and keep adding the remaining characters until finished
xCoordQuote = round(x * .36)
yCoordQuote = round(y * .10)
offsetQuote = 10

#Create coordinates for the quote at the bottom
xCoordBrand = xCoordQuote * .8
yCoordBrand = yCoordQuote * 2.0  
offsetBrand= offsetQuote - 2

xOff = 0
yOff = 0

#Branding
drawing.text((xCoordBrand,yCoordBrand),"Persistance X Passion",(0,0,0),font=subTextFont)
drawing.text((xCoordBrand-offsetBrand,yCoordBrand-offsetBrand),"Persistance X Passion",(255,255,255),font=subTextFont)

#Quote Loop
for token in wrapCont:

    drawing.text((xCoordQuote+xOff,yCoordQuote+yOff),token,(0,0,0),font=font)
    drawing.text(((xCoordQuote+xOff)-offsetQuote,(yCoordQuote+yOff)-offsetQuote),token,(255,255,255),font=font)
    
    if xCoordQuote+xOff > x:
        #New Line
        yCoordQuote *= .20

        #Reset space
        xOff = 0
    
    xOff+=300


#image.show()

#Save Image
#testImg.save("a_test.png")