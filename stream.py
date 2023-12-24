import cv2

usr = "admin"
pwd = "[password]"
ip = "192.168.0.1" # default for access-point mode
cap = cv2.VideoCapture(f"rtsp://{usr}:{pwd}@{ip}/camera-test")

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
