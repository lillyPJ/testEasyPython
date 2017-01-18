import os
import numpy as np
import cv2
from pylab import *
# read from txt file
txtfile = '/home/lili/codes/testPython/txt/val.txt'
txtfile_new = os.path.splitext(txtfile)[0] + '_new.txt'
#open, read file
with open(txtfile, 'r') as f:
    lines = f.readlines()
# read imgnames, points, get the boundingboxes and mini area rectangles
imgnames = []
boundingboxes = []
minareaboxes = []
points = []
for each in lines:
    templist = each.split(' ')
    imgnames.append(templist[0])
    point = np.array([int(x) for x in templist[1:9]])
    point = point.reshape([4, 1, 2])
    points.append(point)
    tempbox = cv2.boundingRect(point)
    boundingboxes.append(tempbox)
    tempbox = cv2.minAreaRect(point)
    minareaboxes.append(tempbox)
# show imgnames, draw points, draw boundingboxes, draw mini area rectangles
imgdir = '/home/lili/codes/testPython/images/jpg/'
for imgname, bbox, mbox, ps in zip(imgnames, boundingboxes, minareaboxes, points):
    img = cv2.imread(imgdir + str(imgname))
    # draw bounding box rectangle
    cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255, 0), 1)
    # draw mini area rectangle (four points that can form a rectangle are ok) box = ps
    box = cv2.cv.BoxPoints(mbox)
    box = np.int0(box)
    cv2.drawContours(img,[box],0,(0,255,255),2)
    # draw points
    imshow(img)
    xys = ps.reshape([4,2])
    plot( xys[:,0],xys[:,1],'r*')
    print( ps.reshape([2, 4]))
    show()
    print imgname
