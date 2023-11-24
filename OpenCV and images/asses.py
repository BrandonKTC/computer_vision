import cv2
import numpy as np

# variables
drawing = False

# function
def draw_circle(event, x,y, flags, param):
    global drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        
        drawing = True
        
    elif event == cv2.EVENT_MBUTTONDOWN:
        if drawing == True:
            
            cv2.circle(img, (x,y) , 100, (0,0,255))
            
    elif event == cv2.EVENT_LBUTTONUP:
        
        drawing = False
        
        cv2.circle(img, (x, y),100, (0,0,255))
    

cv2.namedWindow('dog')
cv2.setMouseCallback('dog',draw_circle)

# showing img with OpenCV

img = cv2.cvtColor(cv2.imread('dog_backpack.jpg'), cv2.COLOR_BGR2RGB)

while True:
    
    cv2.imshow('dog',img)
    
    if cv2.waitKey(1) & 0XFF == 27:
        break

cv2.destroyAllWindows()

