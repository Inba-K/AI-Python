import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.BGR2GREYSCALE)
    faces=face_cascade.detectMultiScale(grey,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Face Detection", faces)
    if cv2.waitKey(1)&ord("q"):
        break
cap.release()
cv2.destroyAllWindows()