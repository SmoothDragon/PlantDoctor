import cv2 as cv
import datetime
import time
# initialize the camera

while True:
    for i in [0,2,4]:
        cam = cv.VideoCapture(i)   # 0 -> index of camera
        s, img = cam.read()
        if s:    # frame captured without any errors
            # cv.namedWindow("cam-test", cv.WINDOW_AUTOSIZE)
            # cv.imshow("cam-test%d"%i,img)
            # cv.waitKey(0)
            # cv.destroyWindow("cam-test%d"%i)
            now = datetime.datetime.now()
            filename = now.isoformat() + '_camera_%d.jpg'%i
            print('Writing file %s'%filename)
            cv.imwrite(filename,img) #save image
    sleep_seconds = 5
    print('Sleeping for %d seconds.'%sleep_seconds)
    time.sleep(sleep_seconds)
