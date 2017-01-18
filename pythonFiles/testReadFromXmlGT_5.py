#!/usr/bin/env python
'''testXmlRead_5: read xml file'''

import xml.etree.ElementTree as ET
from showSection import *
from PIL import Image

def readBoxFromXml(xmlfile):
    tree = ET.ElementTree(file=xmlfile)
    root = tree.getroot()
    imgs = []
    boxes = []
    for eachImg in root:
        img = eachImg[0].text
        nbox = int(eachImg[2].attrib['nTaggedRectangle'])
        box = []
        for ibox in range(nbox):
            x = int(eachImg[2][ibox].attrib['x'])
            y = int(eachImg[2][ibox].attrib['y'])
            w = int(eachImg[2][ibox].attrib['width'])
            h = int(eachImg[2][ibox].attrib['height'])
            box.append([x, y, w, h])
        imgs.append(img)
        boxes.append([nbox, box])
    imgBoxes = dict(zip(imgs, boxes))
    return imgBoxes


if __name__ == '__main__':
    xmlfile = '/home/lili/datasets/ICDAR2011/gt/test/xml/word.xml'
    imgBoxes = readBoxFromXml(xmlfile)
    imgDir = '/home/lili/datasets/ICDAR2011/img/'
    for img in imgBoxes:
        imgName = imgDir + img
        #nbox = imgBoxes[imgName][0]
        box = imgBoxes[img][1]
        image = Image.open(imgName)
        plt.imshow(image)
        displayBoxes(box)
        plt.show()
        print imgName

