# --> Imports
import cv2
import numpy as np
from PIL import Image, ImageDraw

# Открытие и чтение фото с измененнием цветовой патитры с RGB до HSV 
PATH = "Tasks\Task2\IMG_0296.JPG"
img = cv2.imread(PATH)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Создание масок цветов
mask_blue = cv2.inRange(imgHSV,np.array([94,45,0]),np.array([160,255,255]))
mask_red  = cv2.inRange(imgHSV,np.array([0, 220, 94]),np.array([255, 255, 255]))

# Наложение маски
box_red_mask = Image.fromarray(mask_red)
box_blue_mask = Image.fromarray(mask_blue)

# Поиск координат для Box'а
box_r = box_red_mask.getbbox()
box_b = box_blue_mask.getbbox()


# поиск координат центра наждого обьекта
connectivity = 8
num_labels_b, labels_b, stats_b, centroids_blue = cv2.connectedComponentsWithStats(mask_blue , connectivity , cv2.CV_32S)
num_labels_r, labels_r, stats_r, centroids_red = cv2.connectedComponentsWithStats(mask_red , connectivity , cv2.CV_32S)

#Отрисовывание Box'a для каждого цвета на фото
if box_r is not None:
    x1, y1, x2, y2 = box_r
    frame = cv2.rectangle(img, (x1,y1), (x2,y2), (255, 0, 255), 5)
    cv2.putText(frame, f'Red', (x2, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))
    cv2.putText(frame, f'x - {int((x1+x2)/2)} y - {int((y1+y2)/2)}', (x2, y1+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))


if box_b is not None:
    x1, y1, x2, y2 = box_b
    frame = cv2.rectangle(img, (x1,y1), (x2,y2), (0, 255, 255), 5)
    cv2.putText(frame, 'Blue', (x2, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))

cv2.imshow('Origin', frame)
# cv2.imwrite('new.png', img)


cv2.waitKey(0)
