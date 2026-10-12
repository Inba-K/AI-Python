import cv2
img=cv2.imread("300mph.png")
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
(height, width) = img.shape[:2]
center=(width//2,height//2)
M=cv2.getRotationMatrix2D(center,45,1)
rotation=cv2.warpAffine(grey,M,(width,height))
crop=rotation[300:1400,700:1400]
bright=cv2.convertScaleAbs(crop, alpha=1.0, beta=50)
cv2.imshow("Original",img)
cv2.imshow("Greyscale",grey)
cv2.imshow("Rotated",rotation)
cv2.imshow("Cropped",crop)
cv2.imshow("Brightened",bright)
cv2.imwrite("300mph_mogging.png",bright)
cv2.waitKey(0)
cv2.destroyAllWindows()