# --> Imports
import cv2
import time
import numpy as np
from PIL import Image, ImageDraw


class DetectBox:
    """Определение объектов на фото"""
    def __init__(self, PATH):
        self.img = cv2.imread(PATH)


    def draw(self, frame, contours, color):
        """Функция для отрисовывания объекта и его координат"""

        # Перебираем все найденные контуры в цикле
        for cnt in contours:
            rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат

            area = int(rect[1][0] * rect[1][1])  # вычисление площади
            # не продолжаем расчет для маленьких площадей (информационный мусор)
            if area < 10000:
                continue

            sum_x = 0.0
            sum_y = 0.0
            for point in box:
                x = float(point[0])
                y = float(point[1])
                sum_x += x
                sum_y += y
            xc = int(sum_x / float(len(box)))
            yc = int(sum_y / float(len(box)))

            cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)  # рисуем прямоугольник
            # не отрисовываем для маленьких площадей
            if area > 25000:
                cv2.circle(frame, (xc, yc), 5, (0, 255, 0), -1)
                cv2.putText(frame, color, (xc + 10, yc + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
                cv2.putText(frame, f'x - {int((xc + 30) / 2)} y - {int((yc + 30) / 2)}', (xc, yc + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))


    def execute(self):
        """Основная исполнительная функция"""
        imgHSV = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV) # Перевод в цветовой спектр HSV

        # Маски цветов
        mask_blue = cv2.inRange(imgHSV, np.array([94, 45, 0]), np.array([160, 255, 255]))
        mask_red = cv2.inRange(imgHSV, np.array([0, 220, 94]), np.array([255, 255, 255]))

        # Поиск контуров
        contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.draw(self.img, contours_blue, 'Blue')
        self.draw(self.img, contours_red, 'Red')

        cv2.imwrite('Tasks/Task2/new.png', self.img) # Сохранение нового фото
        cv2.imshow('img', self.img)
        cv2.waitKey(0)


if __name__ == '__main__':
    detect_box = DetectBox(r"Tasks/Task2/_IMG_0296.JPG")
    detect_box.execute() 