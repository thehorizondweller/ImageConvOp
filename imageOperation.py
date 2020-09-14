#!/usr/bin/env python3

from PIL import Image
import os

#Source Directory from where we will read TIFF images
sourceDir = "./images/"

#Destination Directory to where we save our processed images
destDir = "./opt/icons/"

def imageOp(im):
  '''
  This function induces the necessary corrections which are required.
  1. Resizing the icons to  128 x 128
  2. Rotating them back to straight position.
  '''
  output = im.resize((128,128))
  output = output.rotate(-90)
  return output

if __name__ == "__main__":
  for imageFile in os.listdir(sourceDir):
    if imageFile.startswith('ic'):
        im = Image.open(sourceDir + imageFile) #Create image object
        im_RGB = im.convert('RGB') #Convert mode to RGB to allow format conversi$
        #Perform the necessary corrections required
        output = imageOp(im_RGB)
        output.save(destDir + imageFile, format='JPEG')
