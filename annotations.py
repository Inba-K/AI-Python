import cv2
img=cv2.imread("300mph.png")
cv2.rectangle(img,(100,100),(200,200),(0,255,0),2)
cv2.circle(img,(500,500),100,(255,0,0),-1)
cv2.line(img,(300,300),(500,600),(0,0,255),2)
cv2.putText(img,"I am going fast",(350,100),cv2.FONT_HERSHEY_SIMPLEX,1,(60,60,60),2)
cv2.imshow("300mph.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()