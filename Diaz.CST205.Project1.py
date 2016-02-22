#Arthur Diaz, this is project one where you find the median values of all the pixels and use this concept to
#delete the guy from the statue
meme = [] #picture list
redList = []
blueList = []
greenList = []
#to add the pictures to the list
for counter in range (1,10):
  imagePath = 'C:/Users/artd9/Desktop/CST205Proj1/Project 1/'+ str(counter) + '.png'    #Dallas Dituri,Chris Forsythe Reference
  meme.append(makePicture(imagePath))

h = getHeight(meme[1]) #Name of the height value
w = getWidth(meme[1]) #Name of the width value
newPicture = makeEmptyPicture(w,h)#Name of the new picture I want to make

for x in range(0,w):
  for y in range(0,h):
    for memes in range (0,9):
      pixel = getPixel(meme[memes],x,y)
      redList.append(getRed(pixel))
      blueList.append(getBlue(pixel))
      greenList.append(getGreen(pixel))
    firetruck = sorted(redList) #name of the variable that sorts the red
    ocean = sorted(blueList) #name of the variable that sorts the blue
    emerald = sorted(greenList) #name of the variable that sorts the green
    finalFiretruck = firetruck[4] #Gets the median of the red list
    finalEmerald = emerald[4]#Gets the median of the green list
    finalOcean = ocean[4] #Gets the median of the blue list
    newColor = makeColor(finalFiretruck,finalEmerald,finalOcean) #makes the pixel colors from the median of the r,g,b values
    setColor(getPixel(newPicture,x,y), newColor) #sets the color in the picture
    redList = [] #Resets the lists of the redList
    blueList = [] #resets the lists of the blueList
    greenList = [] #resets the lists of the greenList
show(newPicture) #shows the new picture :D
