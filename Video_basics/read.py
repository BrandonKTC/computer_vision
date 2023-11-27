import cv2
import time

# Same command function as streaming, its just now we pass in the file path, nice!
cap = cv2.VideoCapture('../DATA/hand_move.mp4')

# FRAMES PER SECOND FOR VIDEO
fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Always a good idea to check if the video was acutally there
# If you get an error at this step, triple check your file path!!
if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND!')
    

while cap.isOpened():
    
    ret, frame = cap.read()
    
    if ret == True:
        
        # Display the frame at same frame rate of recording
        time.sleep(1/fps)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
        
    # automatically break this whole loop if the video is over.
    else:
        break
        
cap.release()
cv2.destroyAllWindows()
