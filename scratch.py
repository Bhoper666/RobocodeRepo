import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)  # 0 for default camera
fourcc = cv2.VideoWriter.fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter("output.mp4", fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.putText(frame, f"{datetime.now().strftime('%Y')}.{datetime.now().strftime('%m')}.{datetime.now().strftime('%d')} {datetime.now().strftime('%H')}:{datetime.now().strftime('%M'):{datetime.now().strftime('%S')}}", (900, 700),
    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
