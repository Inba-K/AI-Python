import cv2
img=cv2.imread("300mph.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
crop=img[100:400,100:400]
brightness=cv2.convertScaleAbs(img,alpha=1.5,beta=50)
cv2.imshow("Original Image",img)
cv2.imshow("Greyscale Image",grey)
cv2.imshow("RGB Image",rgb)
cv2.imshow("Cropped Image",crop)
cv2.imshow("Brightened Image",brightness)
cv2.waitKey(0)
cv2.destroyAllWindows()