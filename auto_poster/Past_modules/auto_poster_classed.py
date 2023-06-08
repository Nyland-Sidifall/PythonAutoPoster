import PIL
import os
import requests
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

class auto_gen:
    #current directory
    directory = None

    #API/File Information
    apiUrl = None
    fontPath = None
    bgPath = None

    #Background Image Dimensions
    xTotal = 0
    yTotal = 0

    #X axis margins for content
    xLeftM = 0
    xRightM = 0
    
    #Content parsed from API
    content = None
    author = None
    splitCont = None

    #Image
    bgImage = None

    #Size of Fonts
    contentFontSize = 0
    authorFontSize = 0
    brandFontSize = 0

    #Other nums to be deleted in the future
    contentLen = 0
    brContent = None

    def __init__(self, apiUrl, fontPath, bgPath):
        self.apiUrl = apiUrl
        self.fontPath = fontPath
        self.bgPath = bgPath
        self.directory = os.path.dirname(__file__)

    def get_quote():
        #getting the API Quote
        quoteJson = requests.get(apiUrl).json()
        content = quoteJson["content"]
        author = quoteJson["author"]
        contentLen = len(content)
    
    def split_quote():    
        brContent = content.replace('\n',' [br] ')
        splitCont = content.split()
    
    def set_font_size(fSize):
        #Getting the file path of the font
        fontFileName = os.path.join(directory, fontPath)
        font = ImageFont.truetype(fontFileName,fSize)
        
    def get_bg():
        #Load the image & get its length and width
        bgFileName = os.path.join(directory, bgPath)
        bgImage = Image.open(bgFileName)
        xTotal,yTotal = bgImage.size

    #Prep Image for the drawing
    drawing = ImageDraw.Draw(bgImage)

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

        
    bgFileName = 'Background_Images/bg_1.jpg'
    contFont = 175
    subFont = 100
    fontFileLocation = 'Fonts/font_1.ttf'
    api = "http://api.quotable.io/random"
    get_quote(api)
    image.show()


    #Save Image
    #testImg.save("a_test.png")
