import cv2
import numpy as np
camera=cv2.VideoCapture(0)
filter="normal"
redint=255
blueint=255
greenint=100
redinte="ok"
greeninte="ok"
blueinte="ok"
while True:
    key=cv2.waitKeyEx(1)
    ret,frame=camera.read()
    if not ret:
          break
    if key==ord('r'):
        filter="red"
    elif key==ord('g'):
        filter="green"
    elif key==ord('b'):
        filter="blue"

    if key==ord('i'):
        redinte="more"
    elif key==ord('d'):
        blueinte="less"
    elif key==2490368:
        greeninte="more"
    elif key==2621440:
        redinte="less"

    if redinte=="more":
        redint+=10
        redinte="ok"
    elif redinte=="less":
        redint-=10
        redinte="ok"
    if blueinte=="less":
        blueint-=10
        blueinte="ok"
    if greeninte=="more":
        greenint+=10
        greeninte="ok"


    if filter=="red":
        red=np.zeros_like(frame)
        red[:,:,2]=redint
        output=cv2.addWeighted(frame,0.7,red,0.3,0)
    elif filter=="green":
        green=np.zeros_like(frame)
        green[:,:,1]=greenint
        output=cv2.addWeighted(frame,0.7,green,0.3,0)
    elif filter=="blue":
        blue=np.zeros_like(frame)
        blue[:,:,0]=blueint
        output=cv2.addWeighted(frame,0.7,blue,0.3,0)
    else:
        output=frame
    cv2.imshow("Live Filters",output)
    if key==ord('q'):
          break
camera.release()
cv2.destroyAllWindows()