import PIL
import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

#Getting the file path of the font
dirname = os.path.dirname(__file__)
fontFileName = os.path.join(dirname, 'Fonts/font_1.ttf')
font = ImageFont.truetype(fontFileName,350)
subTextFont = ImageFont.truetype(fontFileName,150)


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
xCoordQuote = round(x * .08)
yCoordQuote = round(y * .10)
offsetQuote = 10

#Create coordinates for the quote at the bottom
xCoordBrand = xCoordQuote * 3.4
yCoordBrand = yCoordQuote * 9.3  
offsetBrand= offsetQuote - 2

#Main Quote
drawing.text((xCoordQuote,yCoordQuote),"Some Random Quote",(0,0,0),font=font)
drawing.text((xCoordQuote-offsetQuote,yCoordQuote-offsetQuote),"Some Random Quote",(255,255,255),font=font)

#Branding
drawing.text((xCoordBrand,yCoordBrand),"Persistance X Passion",(0,0,0),font=subTextFont)
drawing.text((xCoordBrand-offsetBrand,yCoordBrand-offsetBrand),"Persistance X Passion",(255,255,255),font=subTextFont)

image.show()

#Save Image
#testImg.save("a_test.png")