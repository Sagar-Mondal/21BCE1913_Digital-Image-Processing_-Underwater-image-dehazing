import os
import numpy as np
import cv2
import natsort

from LabStretching import lab_stretching
from RGBStretching import rgb_stretching

np.seterr(over='ignore')
if __name__ == '__main__':
    pass

folder = "C:/Users/sagar/Documents/DIP_Final_review/dehazing/Underwater Image Enhancement/"
path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        img = cv2.imread('C:/Users/sagar/Documents/DIP_Final_review/dehazing/Underwater Image Enhancement/InputImages/15003.png')

        height = len(img)
        width = len(img[0])

        img = rgb_stretching(img)

        img = lab_stretching(img)

        cv2.imwrite('C:/Users/sagar/Documents/DIP_Final_review/dehazing/Underwater Image Enhancement/InputImages/output_img_.png', img)
