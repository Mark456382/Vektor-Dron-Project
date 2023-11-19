# --> Imports 
from PIL import Image


# Словарь изображений
images = {}

# Внесение элементов в словарь изображений 
n = 0
while True:
    n+=1
    name = input("Введите пути до фото через Enter. После окончания ввода введите 'break'")
    if name == 'break':
        break 
    else:
        images[n] = name 


# Словарь цветов
colors = {'Blue': (0, 0, 255, 255),
        'Green': (0, 255, 0, 255),
        'Red': (255, 0, 0, 255)}


def get_key(d: dict[str], value: int) -> None:
    """Получение ключа в словаре по значению"""
    for k, v in d.items():
        if v == value:
            return k


def task_1() -> None:
    """Перебор и сообтношение цветов пикселей с цветами в словаре"""
    for num, image in images.items():
        with Image.open(image) as img:
            img.load()
            color = img.getpixel((5, 5))
            print(f'{num} --- {get_key(colors, color)}')


if __name__ == '__main__':
    task_1()
