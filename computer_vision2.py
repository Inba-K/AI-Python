import cv2
img=cv2.imread("300mph.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
crop=img[100:400,100:400]
brightness=cv2.convertScaleAbs(img,alpha=1.5,beta=50)
(height, width) = img.shape[:2]
center=(width//2,height//2)
M=cv2.getRotationMatrix2D(center,45,1)
rotation=cv2.warpAffine(img,M,(width,height))
cv2.imshow("Original Image",img)
cv2.imshow("Greyscale Image",grey)
cv2.imshow("RGB Image",rgb)
cv2.imshow("Cropped Image",crop)
cv2.imshow("Brightened Image",brightness)
cv2.imshow("Rotated Image",rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()