# --> Imports
import numpy as np
import keras.losses
import keras.datasets.mnist
import keras.utils
import keras.optimizers
from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense


num_classes = 10 # Количество объектов для классификации
input_file = (28, 28, 1) # Размерность данных

# Преобразование и переработка данных mnist, так как приложенный
#  к заданию датасет не разбит по классам и неудобен для обучения нейронной сети

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# Преобразование классов в матрицы

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes) 

# Трансформация данных mnist

x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


def gen_model():
    """Структура нейронной сети"""

    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_file))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
    return model
