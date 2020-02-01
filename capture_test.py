from cv2 import *
# initialize the camera

for i in [0,2,4]:
    cam = VideoCapture(i)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        #namedWindow("cam-test",WINDOW_AUTOSIZE)
        #imshow("cam-test%d"%i,img)
        #waitKey(0)
        #destroyWindow("cam-test%d"%i)
        imwrite("test%d.jpg"%i,img) #save image
