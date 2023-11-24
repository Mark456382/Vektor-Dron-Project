import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model(str(input('Введите путь до обученной модели => ')))

answer = ''

while True:
    path = str(input('Введите путь до изображения или нажмите enter => '))
    if path == '':
        break
    # Загрузка изображений и их трансформация для поддержки нейронной сетью
    image = tf.keras.preprocessing.image.load_img(path, target_size=(28, 28), color_mode='grayscale')
    image = np.expand_dims(image, axis=0)
    image = 1 - image/255.0
    image = image.reshape(1, 28, 28, 1)
    # Определение цифры на изображении
    prediction = model.predict([image])[0]
    print(np.argmax(prediction), max(prediction)*100, '%')
    answer+=str(np.argmax(prediction))

print("Ответ -", answer)