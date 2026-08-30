import cv2
img=cv2.imread("300mph.png")
cv2.arrowedLine(img,(100,100),(800,800),(100,255,255),4,4)
cv2.arrowedLine(img,(800,800),(100,100),(100,255,255),4,4)
cv2.imshow("300mph.png",img)
cv2.imwrite("mod_300mph.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()