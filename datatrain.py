import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from livelossplot.keras import PlotLossesCallback
from tensorflow.keras.preprocessing.image import ImageDataGenerator

classifer = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation=tf.nn.relu, input_shape=(128, 128, 3)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Conv2D(256, (3, 3), activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.MaxPool2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])

classifer.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['acc'])

train_datagen = ImageDataGenerator(rescale=1./255.)
train_datagen = train_datagen.flow_from_directory(
    "dataset/training/",
    target_size=(128, 128),
    batch_size=10,
    class_mode='categorical'
)

validation_datagen = ImageDataGenerator(rescale=1./255.)
validation_datagen = validation_datagen.flow_from_directory(
    "dataset/validation/",
    target_size=(128, 128),
    batch_size=128,
    class_mode='categorical'
)

history = classifer.fit_generator(
    train_datagen,
    steps_per_epoch=8,
    epochs=50,
    validation_data=validation_datagen,
    validation_steps=2
    #callbacks=[PlotLossesCallback()]
)

classifer.save('model500.h5')