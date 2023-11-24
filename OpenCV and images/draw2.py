import cv2
import numpy as np

# FUNCTION

def draw_circle(event, x,y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
    
    elif event == cv2.EVENT_RBUTTONDOWN:
        
        cv2.circle(img, (x,y), 100, (0,0,255), -1)

cv2.namedWindow('draw2')
cv2.setMouseCallback('draw2', draw_circle)

# SHOWING IMG WITH OPENCV

img = np.zeros((512,512,3), dtype=np.int8)

while True:
    
    cv2.imshow('draw2', img)
    
    if cv2.waitKey(20) & 0XFF == 27:
        
        break

cv2.destroyAllWindows()

