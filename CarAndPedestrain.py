import cv2
#image
#img = "images/cars.png"
video = cv2.VideoCapture("images/p.mp4")
#pre defined
detect = "CarDetector.xml"
pedestrain_tracker = "haarcascade_fullbody.xml"
#classifier
carcv = cv2.CascadeClassifier(detect)
Ptracker = cv2.CascadeClassifier(pedestrain_tracker)


#run forever
while True:

  #read current frame
    (successful,frame) = video.read()

    if successful:
        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    #detect cars
    cars = carcv.detectMultiScale(gray_scale)
    pedestrains = Ptracker.detectMultiScale(gray_scale)
    #draw rectngle
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x+1,y+2),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    #draw rectngle
    for (x,y,w,h) in pedestrains:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    #display
    cv2.imshow("video car",frame)
    #donot auto close
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
video.release()

print("code complete")




'''
import cv2
#image
#img = "images/cars.png"
video = cv2.VideoCapture("images/car-video.mp4")
#pre defined
detect = "CarDetector.xml"
#classifier
carcv = cv2.CascadeClassifier(detect)
#run forever
while True:

  #read current frame
    (successful,frame) = video.read()

    if successful:
        gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    #detect cars
    cars = carcv.detectMultiScale(gray_scale)
    #draw rectngle
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #display
    cv2.imshow("video car",frame)
    #donot auto close
    cv2.waitKey(1)
----
#classifier
carcv = cv2.CascadeClassifier(detect)
#grayscale
b_n_w = cv2.cvtColor(imgcv,cv2.COLOR_BGR2GRAY)
#detect cars
cars = carcv.detectMultiScale(b_n_w)
print(imgcv)
#draw rectngle
for (x,y,w,h) in cars:
    cv2.rectangle(imgcv,(x,y),(x+w,y+h),(0,0,255),2)
#display
cv2.imshow("cars",imgcv)

#autoclose stopping
cv2.waitKey()
'''

