from PIL import ImageGrab
import cv2
import time, numpy as np

def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    while (True):
        # 800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))

        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('window', screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()