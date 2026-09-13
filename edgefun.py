import cv2
import numpy as np
camera=cv2.VideoCapture(0)
filter="normal"
while True:
    ret,frame=camera.read()
    key=cv2.waitKey(1)
    if not ret:
        break
    if key==ord('g'):
        filter="gray"
    if key==ord('b'):
        filter="blur"
    if key==ord('r'):
        filter="red"
    if key==ord('s'):
        filter="sepia"
    if key==ord('f'):
        filter="flip"
    if filter=="gray":
        output=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    elif filter=="blur":
        output=cv2.GaussianBlur(frame,(15,15),0)
    elif filter=="red":
        red=np.zeros_like(frame)
        red[:,:,2]=255
        output=cv2.addWeighted(frame,0.7,red,0.3,0)
    elif filter=="sepia":
        kernel=np.array([
            [0.272,0.534,0.131],
            [0.349,0.686,0.168],
            [0.393,0.769,0.189]
        ])
        output=cv2.transform(frame,kernel)
        output=np.clip(output,0,255).astype(np.uint8)
    elif filter=="flip":
        output=frame.copy()
        output[:,10:]=frame[:,:-10]
        output[:,:10]=frame[:,-10:]
    else:
        output=frame
    cv2.imshow("Live Filters",output)
    if key==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()