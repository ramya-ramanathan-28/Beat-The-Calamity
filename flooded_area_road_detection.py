import cv2
import numpy as np
from skimage.morphology import skeletonize,thin
from skimage.util import invert


def road_detection(fname):
    #fname = 'flooded2.jpg'
    im1 = cv2.imread(fname,0)


    #cv2.imshow('',im1)
    #cv2.waitKey(0)

    '''
    im = cv2.Canny(im,200,400)


    cv2.imshow('',im)
    cv2.waitKey(0)



    im = cv2.medianBlur(im, 5)

    cv2.imshow('',im)
    cv2.waitKey(0)
    '''

    #im = cv2.threshold(im, 0 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    im = cv2.threshold(im1, 130 , 255, cv2.THRESH_BINARY)



    im=im[1]

    #cv2.imshow('',im)
    #cv2.waitKey(0)

    #im = cv2.medianBlur(im, 5)

    #cv2.imshow('',im)
    #cv2.waitKey(0)


    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im)

    print(nb_components)

    print(stats.shape)

    sizes = stats[1:, -1]; nb_components = nb_components - 1

    min_size = 1000

    img2 = np.zeros((output.shape))
    #for every component in the image, you keep it only if it's above min_size
    for i in range(0, nb_components):
        if sizes[i] >= min_size and sizes[i]<2000:
            img2[output == i + 1] = 1
            #cv2.imshow('',img2)
            #cv2.waitKey(0)
            print(sizes[i])
            #img2 = np.zeros((output.shape))
            

    #cv2.imshow('',img2)
    #cv2.waitKey(0)

    skeleton = skeletonize(img2)

    #skeleton = thin(img2,max_iter=25)



    skeleton = np.array(skeleton, dtype=np.uint8)

    print(skeleton)

    for i in range(len(skeleton)):
        for j in range(len(skeleton[0])):
            if skeleton[i][j]==1:
                skeleton[i][j]=255

    print(skeleton)

    #cv2.imshow('',skeleton)
    #cv2.waitKey(0)


    #img2=np.array(img2, dtype=np.uint8)
    image = cv2.Canny(skeleton,100,200)
    '''
    for i in range(len(im)):
        for j in range(len(im)):
            if im[i][j]==1:
                im[i][j]=255
       
    '''
    #cv2.imshow('',image)
    #cv2.waitKey(0)


    #new_img = Image.blend(im, image, 0.5)
    dst = cv2.addWeighted(im1,0.4,image,0.8,0)
    #cv2.imshow('',dst)
    #cv2.waitKey(0)

    cv2.imwrite(r".\static\images\road.jpg",dst)






