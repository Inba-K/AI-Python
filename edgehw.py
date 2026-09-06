import cv2
img_name=input("Enter the name of the file:")
img=cv2.imread(img_name,cv2.IMREAD_GRAYSCALE)
edge=input("What edge detection method do you want to use today? Choose lap, can, or sob. ")
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
gauss=cv2.GaussianBlur(img,(5,5),0)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
canny=cv2.Canny(img,100,200)
cv2.imshow("Original",img)
if "lap" in edge:
    cv2.imshow("Laplacian",lap)
elif "can" in edge:
    cv2.imshow("Canny",canny)
elif "sob" in edge:
    cv2.imshow("Sobel_x",sobel_x)
    cv2.imshow("Sobel_y",sobel_y)
else:
    print("Choose lap, can, or sob.")
cv2.waitKey(0)
cv2.destroyAllWindows()