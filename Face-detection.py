import cv2
image=cv2.imread('IMG_20240810_153718.jpg')
image = cv2.resize(image,(200,400))
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
pos = classifier.detectMultiScale(grey_img)
for x,y,w,h in pos:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,300,0),3)
cv2.imshow("Face Detection",image)
while True:
    key = cv2.waitKey(1)
    if key == 'q':
        cv2.destroyAllWindows()
        break