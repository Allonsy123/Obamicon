from PIL import Image #change IMAGENAME to the path on your computer to the image you're using



#print (im.size) #Get the width and hight of the image for iterating over
#pix[x,y] = value # Set the RGBA Value of the image (tuple)
#print (pix[x,y]) #Get the RGBA Value of the a pixel of an image


# RGB values for recoloring.
lightGrey = (211, 211, 211)
Grey = (144, 144, 144)
darkGrey = (88, 88, 88)


# Import image.

my = Image.open("Backgroundp.png")
image_list = my.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.


recolored = [] #list that will hold the pixel data for the new image.



#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

for pixel in image_list:

    intensity = pixel[0]+pixel[1]+pixel[2]

    if intensity <= 701:
        recolored.append(darkGrey)
    if 701 < intensity <= 900:
        recolored.append(lightGrey)
    if 900 < intensity <= 950:
        recolored.append(lightGrey)
    if intensity > 950:
        recolored.append(lightGrey)




# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("Off_Back1.jpg", "jpeg") #save the new image as "recolored.jpg"
