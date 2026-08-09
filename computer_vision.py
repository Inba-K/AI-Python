import cv2
img=cv2.imread("300mph.png")
res=cv2.resize(img,(200,200))
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",res)
cv2.imshow("Grey image",grey)
cv2.waitKey(0)