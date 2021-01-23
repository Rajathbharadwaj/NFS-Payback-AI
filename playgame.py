import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey,ReleaseKey, turnRight, turnLeft, straight, reverse, reverseLeft, reverseRight, W, A, D
from alexnet import alexnet
from getkeys import key_check

WIDTH = 80
HEIGHT = 60
LR = 0.001
EPOCHS = 15

MODEL_NAME = 'nfspb_epoch_lr{}_{}_{}_reverse.model'.format('0001', 'alexnet', EPOCHS) #model name
model = alexnet(WIDTH, HEIGHT, LR) #init the model architechture
model.load(MODEL_NAME) #load the pretrained model


def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    paused = False
    while (True):

        if not paused:
            # 800x600 windowed mode
            screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640))) #grab the game screen 
            print('loop took {} seconds'.format(time.time() - last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY) #convert to greyscale
            screen = cv2.resize(screen, (80, 60)) #resize as per model accepted dimensions
            cv2.imshow('window', screen)
            moves = list(np.around(model.predict([screen.reshape(80, 60, 1)])[0])) #predict the moves based on the above resized image(array/tensor) -> returns list
            if moves == [1, 0, 0, 0]:
                turnLeft()
                time.sleep(0.09)
                #straight()
                print('Predict to turn left')
            elif moves == [0, 1, 0, 0]:
                straight()
                print('Predict to turn straight')
            elif moves == [0, 0, 1, 0]:
                turnRight()
                time.sleep(0.09)
                #straight()
                print('Predict to turn Right')
            elif moves == [0, 0, 0, 1]:
                reverse()
                time.sleep(0.5)
                print('Reverse')
            elif moves == [1, 0, 0, 1]:
                reverseLeft()
                print('Reverse Left')

            elif moves == [0, 0, 1, 1]:
                reverseRight()
                print("Reverse Right")
            else:
                pass
                print('No moves')

        keys = key_check()

        # to pause the keypress simulation, to gain control over the car.
        if 'J' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
