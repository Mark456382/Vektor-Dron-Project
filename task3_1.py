import cv2
import logging 
import numpy as np
from PIL import Image, ImageDraw


cap = cv2.VideoCapture(r'Tasks\Task3\IMG_0298.MP4')

while True:
    ret, frame = cap.read()

    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(imgHSV,np.array([94,45,0]),np.array([160,255,255]))
    mask_red  = cv2.inRange(imgHSV,np.array([0, 220, 94]),np.array([255, 255, 255]))
    
    contours_blue, hierarchy_blue = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_red, hierarchy_red = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    connectivity = 8
    num_labels_b, labels_b, stats_b, centroids_blue = cv2.connectedComponentsWithStats(mask_blue , connectivity , cv2.CV_32S)
    num_labels_r, labels_r, stats_r, centroids_red = cv2.connectedComponentsWithStats(mask_blue , connectivity , cv2.CV_32S)
    
    box_red_mask = Image.fromarray(mask_red)
    box_blue_mask = Image.fromarray(mask_blue)

    box_r = box_red_mask.getbbox()
    box_b = box_blue_mask.getbbox()

    if box_r is not None:
        cv2.drawContours(frame, contours_red, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy_red, 1 )
        
        for i in range(len(centroids_red)-1):
            lst = centroids_red
            xr1, yr1, xr2, yr2 = int(lst[i][0]), int(lst[i][1]), int(lst[i+1][0]), int(lst[i+1][1])

            cv2.circle(frame,(int(xr1),int(yr1)), 5,(255,0,0), -1) 
            cv2.circle(frame,(int(xr2),int(yr2)), 5,(255,0,0), -1)

            cv2.putText(frame, f'Red_1', (xr1, yr1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))
            cv2.putText(frame, f'Red_2', (xr2, yr2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

            cv2.putText(frame, f'x1 - {int(xr1)} y1 - {int(yr1)}', (xr1+10, yr1+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))
            cv2.putText(frame, f'x2 - {int(xr2)} y2 - {int(yr2)}', (xr2+10, yr2+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0 ,0))


    if box_b is not None:
        cv2.drawContours(frame, contours_blue, -1, (0,0,255), 3, cv2.LINE_AA, hierarchy_blue, 1 )

        for i in centroids_blue[1::2]:
            xb, yb = int(i[0]), int(i[1])
            cv2.circle(frame,(xb,yb), 5,(0,0,255), -1) 

            cv2.putText(frame, f'Blue', (xb, yb), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))
            cv2.putText(frame, f'x - {xb} y - {yb}', (xb+10, yb+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0 ,255))


    if ret:
        cv2.imshow('vid', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()