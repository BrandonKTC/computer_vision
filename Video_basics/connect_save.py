import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# MACOS AND LINUX: *'XVID' (MacOS users may want to try VIDX as well just in case)
# WINDOWS *'VIDX'
writer = cv2.VideoWriter('awesomevideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), 25, (width,heigth))

while True:
    
    ret, frame = cap.read()
    
    # Write the video
    writer.write(frame)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# release camera, writer & destroy all windows
cap.release()
writer.release()
cv2.destroyAllWindows()
