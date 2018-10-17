# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
import os
import numpy as np
def ConvertBlue(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#for (lower, upper) in boundaries:
		#lower = np.array(lower, dtype = "uint8")
		#upper = np.array(upper, dtype = "uint8")
 
		# find the colors within the specified boundaries and apply
		# the mask
	#lower = np.array([100,50,50])
	lower = np.array([100,150,0])
	upper = np.array([140,255,255])
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
	#cv2.imshow("images",output)
	#cv2.waitKey(0)
	return(output)
	
# construct the argument parse and parse the arguments

def imageCompare(first, second):
        # load the two input images
        imageA = cv2.imread(first)
        for i in range(255):
                imageA[np.where((imageA == [i,i,i]).all(axis = 2))] = [255, 0, 0]
        #cv2.imshow("imageA Modified",imageA)
        imageB = cv2.imread(second)
        outputA = ConvertBlue(imageA)
        outputB = ConvertBlue(imageB)


        # convert the images to grayscale
        grayA = cv2.cvtColor(outputA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(outputB, cv2.COLOR_BGR2GRAY)

        #cv2.imshow("intermediate2", grayB- grayA)
        #cv2.waitKey(0)



        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        # loop over the contours
        for c in cnts:
                        # compute the bounding box of the contour and then draw the
                        # bounding box on both input images to represent where the two
                        # images differ
                        (x, y, w, h) = cv2.boundingRect(c)
                        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
         
        # show the output images
        #cv2.imshow("Original", imageA)
        #cv2.imshow("Modified", imageB)
        #cv2.imshow("Diff", diff)
        #cv2.imshow("Thresh", thresh)

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        cv2.imwrite('output2.png',diff)
        from PIL import Image
        import sys

        im = Image.open("output2.png")
        im = im.convert('RGB')
        pixdata = im.load()
        print(im.size)
        #print(pixdata[x,y])
        #for pixel in im.getdata():

        for y in range(im.size[1]):
            for x in range(im.size[0]):
                '''RGB= im.getpixel((x,y))
                R,G,B = RGB
                if G!= 255:
                    R = 255
                im.setpixel((x,y))=(R,G,B)'''
                #print(RGB)
                if pixdata[x, y] == (0, 0, 0):
                    if x+10<im.size[0]:
                        for xn in range(x+1, x+11):
                            if pixdata[xn, y] != (0,0,0) and pixdata[xn, y] != (255, 0, 0):
                                pixdata[xn, y] = (255, 210, 0)
                    if x-10>=0:
                        for xn in range(x-10, x):
                            if pixdata[xn, y] != (0,0,0) and pixdata[xn, y] != (255, 0, 0):
                                pixdata[xn, y] = (255, 210, 0)
                    if y+10<im.size[1]:
                        for yn in range(y+1, y+11):
                            if pixdata[x, yn] != (0,0,0) and pixdata[x, yn] != (255, 0, 0):
                                pixdata[x, yn] = (255, 210, 0)
                    if y-10>=0:
                        for yn in range(y-10, y):
                            if pixdata[x, yn] != (0,0,0) and pixdata[x, yn] != (255, 0, 0):
                                pixdata[x, yn] = (255, 210, 0)
                        
                    pixdata[x, y] = (255, 0, 0)
                    

        im.save("red_coloured.png")
        im = Image.open("red_coloured.png")
        im = im.convert('RGB')
        pixdata = im.load()
        print(im.size)
        #print(pixdata[x,y])
        #for pixel in im.getdata():

        for y in range(im.size[1]):
            for x in range(im.size[0]):
                if pixdata[x, y] != (255, 0, 0) and pixdata[x, y] != (255, 210, 0):
                    pixdata[x, y] = (0, 255, 0)
                    

        im.save("./static/images/final.png")
        background = Image.open("./static/images/before.jpg").convert('RGBA')
        foreground = Image.open("./static/images/final.png").convert('RGBA')
        foreground.putalpha(96)

        background.paste(foreground, (0,0) , foreground)
        background.save("./static/images/final3.png")
        return background            


