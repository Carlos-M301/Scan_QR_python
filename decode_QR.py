import cv2 as cv
#Set Camera object
cam = cv.VideoCapture(0)

#QR detection
detect = cv.QRCodeDetector()

while True:
    #get image
    _, img = cam.read()
    #get bounding box and data
    data, bbox, _ = detect.detectAndDecode(img)
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        for i in range(len(bbox)):
            cv.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color= (255,
                    0,255), thickness=2)
        if data:
            cv.putText(img, 'Captured!', (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("data is =", data)
        # display the image preview
    cv.imshow('code detector', img)
    if(cv.waitKey(1) == ord("q")):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()

#retval, points, straight_qrcode = detect.detectAndDecode(img)

#print(retval)