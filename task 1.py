# --> Imports 
from PIL import Image


# Словарь изображений
images = {1: r'Tasks\Task1\blue.png', 
        2: r'Tasks\Task1\green.png', 
        3: r'Tasks\Task1\red.png'}

# Словарь цветов
colors = {'Blue': (0, 0, 255, 255),
        'Green': (0, 255, 0, 255),
        'Red': (255, 0, 0, 255)}


def get_key(d, value):
    """Получение ключа в словаре по значению"""
    for k, v in d.items():
        if v == value:
            return k


def task_1():
    # Перебор и сообтношение цветов пикселей с цветами в словаре
    for num, image in images.items():
        with Image.open(image) as img:
            img.load()
            color = img.getpixel((5, 5))
            print(f'{num} --- {get_key(colors, color)}')


if __name__ == '__main__':
    task_1()
