# Create a function based on a CV2 Event (Left button click)
import cv2


# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked,color

    # get mouse click on down and track center
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN :
        
        clicked = True
        center = (x,y)
        
        if event == cv2.EVENT_LBUTTONDOWN:
            
            color = (255,0,0)
        
        else:
            
            color = (0,0,255)
        
            
    # Use boolean variable to track if the mouse has been released
    if event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        
        clicked = False

        
# Haven't drawn anything yet!
color = (0,0,0)
center = (0,0)
clicked = False


# Capture Video
cap = cv2.VideoCapture(0)

# Create a named window for connections
circle = cv2.namedWindow('circle')
# Bind draw_rectangle function to mouse cliks
drawing = cv2.setMouseCallback('circle',draw_circle)



while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Use if statement to see if clicked is true
    if clicked:
        # Draw circle on frame
        cv2.circle(frame, center, 50, color, 5)
        
    # Display the resulting frame
    cv2.imshow('circle',frame)

    # This command let's us quit with the "q" button on a keyboard.
    # Simply pressing X on the window won't work!
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
        
# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
