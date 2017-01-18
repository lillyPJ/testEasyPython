#!/usr/bin/env python
'''getFileList_2: get all the filenames in the same dir'''

import os
def get_imlist(path, ext = '.jpg'):
    '''return the list of all the files(ext) in the path'''
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(ext)]
## get_imlist function is equal to import glob, img_lists = glob.glob(dir + '/*.jpg')
if __name__ == '__main__':
    for each in get_imlist('/home/lili/codes/testPython/images/jpg'):
        print each