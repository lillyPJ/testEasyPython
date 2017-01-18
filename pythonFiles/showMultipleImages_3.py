#!/usr/bin/env python
'''showMultipleImages_3: show multiple images in one figure'''

from pylab import *
import os
from PIL import Image

def showMultipleImages(imagelist, txtlist = [], nrow = 0, ncol = 0):
    '''show multiple images in one figure, the last three para can be generate automatically'''
    nimg = len(imagelist)
    if not txtlist:
        txtlist = range(1,nimg+1)
    if nrow + ncol < 1:
        nrow = int(floor(sqrt(nimg)))
        ncol = int(ceil(nimg / (nrow + 0.00001)))
    for i in range(nimg):
        subplot(nrow,ncol,i + 1)
        imshow(imagelist[i])
        title(txtlist[i])
        axis('off')
    show()



if __name__ == '__main__':
    filedir = '/home/lili/codes/testPython/images/jpg'
    filelist = [os.path.join(filedir, f) for f in os.listdir(filedir) if f.endswith('.jpg')]
    filelist_temp = filelist[:5]
    imagelist = []
    for each in filelist_temp:
        imagelist.append(array(Image.open(each)))
    txtlist = []
    for each in filelist_temp:
        txtlist.append(os.path.splitext(os.path.basename(each))[0])
    showMultipleImages(imagelist, txtlist)
    disp('ok')