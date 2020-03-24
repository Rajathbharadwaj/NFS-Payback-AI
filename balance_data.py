import numpy as np
import pandas as pd
import cv2
from collections import Counter
from random import shuffle

train_data = np.load('training_data_with_reverse.py.npy', allow_pickle=True)

df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []
reverses = []


shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1, 0, 0, 0]:
        lefts.append([img, choice])
    elif choice == [0, 1, 0, 0]:
        forwards.append([img, choice])
    elif choice == [0, 0, 1, 0]:
        rights.append([img, choice])
    elif choice == [0, 0, 0, 1]:
        reverses.append([img, choice])
        print('no matches')


forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
reverses = reverses[:len(forwards)]

final_data = forwards + lefts + rights + reverses
print(len(final_data))
shuffle(final_data)

np.save('training_data_v2_reverse.npy', final_data)

# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test', img)
#     print(choice)
#
#     if cv2.waitKey(25) & 0xFF==ord('q'):
#         cv2.destroyAllWindows()
#         break
