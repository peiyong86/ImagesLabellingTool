#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Usage:
    python labeltoo.py <imagepath> <csvfilename>
Anthor:
    peiyong
Email:
    peiyong86@gmail.com
Date:
    2017.4.21
"""
import os
import sys
import csv
import cv2
from labels import labels_all

def readlabels(filename):
    imagenames = []
    if os.path.isfile(filename):
        with open(filename,'r') as f:
            lines = f.readlines()
            imagenames = [l.split(',')[0] for l in lines]
    return imagenames

def printlabels(labels):
    str_ = []
    for k in labels.keys():
        str_.append("{} for {}".format(chr(k), labels[k]))
    str_ = ' , '.join(str_)
    print("Type key {}".format(str_))

def getanno(labels):
    while(True):
        printlabels(labels)
        k = cv2.waitKey(0)
        if k in labels.keys():
            return labels[k]
        if k==27:
            return None

def main():
    if len(sys.argv)<3:
        print("python {} imagefolder outputfile".format(os.path.basename(__file__)))
        return
    imagefolder = sys.argv[1]
    outputfile = sys.argv[2]
    print("labelling images in {}, and output to {}".format(imagefolder,outputfile))

    labelledimnames = readlabels(outputfile)
    if labelledimnames is not []:
        print("{} contains labelled images: {}".format(outputfile, ','.join(labelledimnames)))

    with open(outputfile,'a') as f:
        writer = csv.writer(f, delimiter=',')
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        for filename in sorted(os.listdir(imagefolder)):
            if filename not in labelledimnames:
                filepath = os.path.join(imagefolder, filename)

                try:
                    im = cv2.imread(filepath)
                    cv2.imshow('image', im)
                    annos = [filename]
                    for labels in labels_all:
                        anno = getanno(labels)
                        if anno is None:
                            return
                        else:
                            annos.append(anno)
                    writer.writerow(annos)
                except:
                    print("{} is not a valid image file!".format(filepath))

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
