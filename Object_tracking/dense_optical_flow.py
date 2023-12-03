import cv2
import numpy as np

# Capture the video
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

prev_img = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)

hsv_mask[:,:,1] = 255

while True:
    
    ret, frame = cap.read()
    
    next_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate the optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_img, next_img, None, .5, 3, 15, 3, 5, 1.2, 0)
    # convert the flow to polar coordinates
    mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1], angleInDegrees=True)
    # assign the hue according to the angle of optical flow
    hsv_mask[:,:,0] = ang/2
    # normalize the magnitude of the flow
    hsv_mask[:,:,2] = cv2.normalize(mag, None, 0,255, cv2.NORM_MINMAX)
    
    bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
    
    cv2.imshow('frame', bgr)
    # if esc key is pressed, break out of the loop
    
    k = cv2.waitKey(10) & 0xFF

    if k == 27:
            break

    # reassign the previous image to the next image based on the flow (if something is moving, it will be the next image)
    prev_img = next_img
    
cv2.destroyAllWindows()
cap.release()