from alexnet import alexnet
import numpy as np

WIDTH = 80
HEIGHT = 60
LR = 0.001
EPOCHS = 1000

MODEL_NAME = 'nfspb_epoch_lr{}_{}_{}_reverse.model'.format('0001', 'alexnet', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

train_data = np.load('training_data_v2_reverse.npy', allow_pickle = True)

train = train_data[:-900]
test = train_data[-900:]

X_train = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y_train = np.array([i[1] for i in train])

X_test = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
Y_test = np.array([i[1] for i in test])

model.fit({'input': X_train}, {'targets': Y_train}, n_epoch=EPOCHS, validation_set=({'input': X_test}, {'targets': Y_test}),
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)
