#!/usr/bin/env python
'''histeq_4: get the histogram equalization image'''
from pylab import *
from PIL import Image
from numpy import *

def histeq(im, nbr_bins = 256):
    '''return the histogram eqation image'''
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf2 = 255 * cdf / cdf[-1]
    im2 = interp(im.flatten(), bins[:-1], cdf2)

    return im2.reshape(im.shape)

if __name__ == '__main__':
    im_pil = Image.open('../images/jpg/0420001.jpg').convert('L')
    im = array(im_pil)
    im2 = histeq(im)
    gray()
    txtlist = ['oriImg', 'histeqImg', 'oriImg_hist', 'histeqImg_hist']
    subplot(2, 2, 1), imshow(im), title(txtlist[0]), axis('off')
    subplot(2, 2, 2), imshow(im2), title(txtlist[1]), axis('off')
    subplot(2, 2, 3), hist(im.flatten(), 256, normed=True), title(txtlist[0]), axis('off')
    subplot(2, 2, 4), hist(im2.flatten(), 256, normed=True), title(txtlist[0]), axis('off')

    show()
    disp('ok')