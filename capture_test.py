import cv2 as cv
import datetime
import time
# initialize the camera
print('start')
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
            if i == 0:
                filename = 'z_N.NPK.P.camera_' + now.isoformat() + '.jpg'
            if i == 4:
                filename = 'z_NPK.P.K.camera_' + now.isoformat() + '.jpg'
            if i == 2:
                filename = 'z_H20.Control_camera_' + now.isoformat() + '.jpg'
                #filename = '_camera_%d.'%i + now.isoformat() + '.jpg'
            print('Writing file %s'%filename)
            cv.imwrite(filename,img) #save image
    sleep_seconds = 21600
    print('Sleeping for %d seconds.'%sleep_seconds)
    time.sleep(sleep_seconds)
