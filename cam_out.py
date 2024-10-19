import cv2

cap = cv2.VideoCapture(0)  # 0 for default camera
fourcc = cv2.VideoWriter.fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("output.avi", fourcc, 30.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Process the frame if necessary (e.g., apply filters, detect objects)

    out.write(frame)

    # Display the frame (optional)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
