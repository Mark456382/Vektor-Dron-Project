import cv2
import numpy as np
from keras.models import load_model

model = load_model(str(input('Введите путь до обученной модели => ')))

answer = ''

while True:
    path = str(input('Введите путь до изображения или нажмите enter => '))
    if path == '':
        break
    # Загрузка изображений и их трансформация для поддержки нейронной сетью
    image = cv2.imread(path, 0)
    image = np.array(image)
    image = image.reshape(1, 28, 28, 1)
    image = image / 255.0
    # Определение цифры на изображении
    prediction = model.predict([image])[0]
    print(np.argmax(prediction), max(prediction))
    answer+=str(np.argmax(prediction))

print(answer)