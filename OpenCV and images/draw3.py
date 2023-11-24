import cv2
import numpy as np

# VARIABLES

# True while mouse button down, False while mouse button UP
drawing = False
ix = -1
iy = -1

# FUNCTION

def draw_rectangle(event, x,y, flags, param):
    
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        
        if drawing == True:
    
            cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), color=(0,0,255), thickness=-1)
    
    elif event == cv2.EVENT_LBUTTONUP:
        
        drawing = False

 #       cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)
    
cv2.namedWindow('draw3')
cv2.setMouseCallback('draw3', draw_rectangle)

# SHOWING IMG WITH OPENCV

img = np.zeros((512,512,3), dtype=np.int8)

while True:
    
    cv2.imshow('draw3',img)
    
    # CHECKS FOR esc Key
    if cv2.waitKey(1) & 0XFF == 27:
        
        break

cv2.destroyAllWindows()

