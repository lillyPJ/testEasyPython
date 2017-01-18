#!/usr/bin/env python
'''changeImgExt_1: change the format of images in the same dir'''

import os
from PIL import Image

def changeImgExt(filedir, inext = '.jpg', outext = '.png'):
    filelist = [os.path.join(filedir, f) for f in os.listdir(filedir) if f.endswith(inext)]
    for infile in filelist:
        outfile = os.path.splitext(infile)[0] + outext
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                print "cannot convert", infile

if __name__ == '__main__':
    changeImgExt('/home/lili/codes/testPython/images/png')
