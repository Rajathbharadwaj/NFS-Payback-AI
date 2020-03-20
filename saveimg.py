import numpy as np
from PIL import ImageGrab
import cv2, time


def record_img():
    # last_time = time.time()
    while(True):
        inc = 0
        image = ImageGrab.grab(bbox=(0, 40, 800, 640))
        image.save(r'G:\gtaplay\delete\img{}.jpg'.format(inc))
        continue
        # img = cv2.imread('G:\gtaplay\delete\img{}.jpg'.format(inc))
        # imgName = 'img{}.jpg'.format(inc)
        # cv2.imwrite(imgName, img)
        # cv2.imshow('window', img)
        # inc = inc+1
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break


if __name__ == '__main__':
    record_img()