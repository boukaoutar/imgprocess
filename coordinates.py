import cv2

def mouse_event(event,x,y,flag,param):

    if(event==cv2.EVENT_LBUTTONDOWN):
        str1=str(x)+","+str(y)
        cv2.putText(image,str1,(x,y),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        cv2.imshow("Frame",image)

image = cv2.imread("test.jpg")
cv2.imshow("Frame",image)
cv2.setMouseCallback("Frame", mouse_event)

cv2.waitKey(0)
cv2.destroyAllWindows()




