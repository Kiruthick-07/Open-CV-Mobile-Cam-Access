import cv2
vid=cv2.VideoCapture(0) # command to fetch video input..paste the url at the position of 0
while True:
    ret,frame = vid.read() # must declare two variable
    resize=cv2.resize(frame,(600,400))# reducing the size of the frame
    cv2.imshow("Test Video Run",resize)
    feed=cv2.waitKey(1)# waitkey must be used for continious streaming
    if feed==ord('a'):
        break
