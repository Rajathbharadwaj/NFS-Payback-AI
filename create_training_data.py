import numpy as np
from PIL import ImageGrab
import cv2
import time
from getkeys import key_check
import os


def keysToOutput(keys):
    #output = [A, W,  D, S]
    output = [0, 0,  0, 0]

    if 'A' in keys:
        output[0]= 1
    elif 'D' in keys:
        output[2] = 1
    elif 'W' in keys:
        output[1] = 1
    elif 'S':
        output[3] = 1
    else:
        pass
    return output

# def mouseToOutput(keys):
#     #output = [x, y,  button]
#     output = [0, 0,  0, 0]
#
#     if 'A' in keys:
#         output[0]= 1
#     elif 'D' in keys:
#         output[2] = 1
#     elif 'W' in keys:
#         output[1] = 1
#     elif 'S':
#         output[3] = 1
#     else:
#         pass
#     return output

file_name = 'training_data_with_reverse.py'

if os.path.isfile(file_name):
    training_data = list(np.load(file_name))
    print('Training data loading...')
else:
    training_data = []


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while (True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        last_time = time.time()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        # resize to something a bit more acceptable for a CNN
        screen = cv2.resize(screen, (80, 60))
        keys = key_check()
        output = keysToOutput(keys)
        training_data.append([screen, output])
        print('Frame took {} secs'.format(time.time() - last_time))

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name, training_data)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



if __name__ == '__main__':
    main()