import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
time.sleep(1)

ret,frame = cap.read()

# grab the first face detection
face_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_frontalface_default.xml')
# return list of all the numpy array where face are detected
face_rects = face_cascade.detectMultiScale(frame)
# grabing the first face
(face_x,face_y,w,h) = tuple(face_rects[0])
# set up the tracking window
track_window = (face_x,face_y,w,h)

# set up ROI
roi = frame[face_y:face_y+h,face_x:face_x+w]
# HSV color mapping
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
# find histogram
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0,180])
# normalize histogram values
cv2.normalize(roi_hist,roi_hist, 0,255, cv2.NORM_MINMAX)
# set up the termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    
    ret, frame = cap.read()
    
    if ret:
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # calculate the back projection
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        #########################################################
        # apply camshift to get the new location
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        # capture pts
        pts = cv2.boxPoints(ret)
        pts = np.intp(pts)
        # draw rectangle with pts
        img2 = cv2.polylines(frame, [pts], True, (0,0,255),5)
        #########################################################
        # show the image
        cv2.imshow('img',img2)
        # if esc press break
        k = cv2.waitKey(1) & 0xFF
        
        if k == 27:
            break
    
cap.release()
cv2.destroyAllWindows()