import cv2
import logging 
import numpy as np
from PIL import Image


cap = cv2.VideoCapture(r'Tasks\Task3\IMG_0298.MP4')


def task_3():
    center_blue_x, center_blue_y = 0, 0
    center_red_x1, center_red_y1 = 0, 0
    center_red_x2, center_red_y2 = 0, 0

    try:
        while True:
            ret, frame = cap.read()
            # Создание масок цветов

            imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            mask_blue = cv2.inRange(imgHSV,np.array([94,45,0]),np.array([160,255,255]))
            mask_red  = cv2.inRange(imgHSV,np.array([0, 220, 94]),np.array([255, 255, 255]))
            
            # Наложение маски
            box_red_mask = Image.fromarray(mask_red)
            box_blue_mask = Image.fromarray(mask_blue)

            # Поиск координат для Box'а
            box_r = box_red_mask.getbbox()
            box_r1 = box_red_mask.getbbox()
            box_b = box_blue_mask.getbbox()

            # поиск координат центра наждого обьекта
            connectivity = 8
            num_labels_b, labels_b, stats_b, centroids_blue = cv2.connectedComponentsWithStats(mask_blue , connectivity , cv2.CV_32S)
            num_labels_r, labels_r, stats_r, centroids_red = cv2.connectedComponentsWithStats(mask_red , connectivity , cv2.CV_32S)

            #Отрисовывание Box'a для каждого цвета на фото
            if box_r is not None:
                x1, y1, x2, y2 = box_r
                frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255, 0, 255), 5)
                cv2.putText(frame, f'Red', (x2, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))
                cv2.putText(frame, f'x1 - {int((x1+x2)/2)} y - {int((y1+y2)/2)}', (x2, y1+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))
                print(f'---{centroids_red}---')

            if box_b is not None:
                x1, y1, x2, y2 = box_b
                frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 255), 5)
                cv2.putText(frame, 'Blue', (x2, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))
                cv2.putText(frame, f'x - {int((x1+x2)/2)} y - {int((y1+y2)/2)}', (x2, y1+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))


            if ret:
                cv2.imshow('Video', frame)
                center_blue_x, center_blue_y = int(centroids_blue[0][0]), int(centroids_blue[0][1])
                center_red_x1, center_red_y1 = int(centroids_red[0][0]), int(centroids_red[0][1])
                # center_red_x2, center_red_y2 = int(centroids_red[1][0]), int(centroids_red[1][1])
                # with cv2.VideoWriter_fourcc(*'XVID') as fourcc:
                #     out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
    except BaseException as e:
        return [[center_blue_x, center_blue_y], [[center_red_x1, center_red_y1], [center_red_x2, center_red_y2]]]
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    info = task_3()
    print(f'''
        Object
        =============================================
        Blue:   x - {info[0][0]} 
                y - {info[0][1]}
        ---------------------------------------------
        Red:    x1 - {info[1][0][0]}
                y1 - {info[1][0][1]}

                x2 - {info[1][1][0]}
                y2 - {info[1][1][1]}
        ''')
