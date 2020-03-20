import numpy as np
from PIL import ImageGrab
import cv2, time
from tensorflow.keras.models import load_model
from directkeys import turnLeft, turnRight, straight
model = load_model("model500.h5")
lst = []
max_lst = []


def direction(maxlist):
    if maxlist.count(0) > (maxlist.count(1) or maxlist.count(2)):
        turnLeft()
        print('letf')
    elif maxlist.count(1) > (maxlist.count(0) or maxlist.count(2)):
        turnRight()
        print('right')
    elif maxlist.count(2) >www (maxlist.count(0) and maxlist.count(1)):
        straight()
        print('straight')
    else:
         print('nothing')
         pass

def screen_record():
    #last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        printscreen = np.resize(printscreen, (1, 128, 128, 3))
        navigation = model.predict(printscreen)
        while len(lst)!=30:
            lst.append(navigation[0])
        arr_list = np.array(lst)

        for i in arr_list:

            max_lst.append(i.argmax())

            #print(cnt)
        direction(max_lst)



        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    screen_record()