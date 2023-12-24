# import cv2

# usr = "admin"
# pwd = "Vfksi13*"
# ip = "192.168.0.3" # default for access-point mode
# cap = cv2.VideoCapture(f"rtsp://{usr}:{pwd}@{ip}/camera-test")

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(20) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

import cv2

usr = "admin"
pwd = "Vfksi13*"
ip = "192.168.0.3"

cap = cv2.VideoCapture(f"rtsp://{usr}:{pwd}@{ip}/live/ch00_1", cv2.CAP_FFMPEG)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
