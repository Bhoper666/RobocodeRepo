import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', (10, 710), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

