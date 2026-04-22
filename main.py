from ultralytics import YOLO
import cv2

from anomaly import check_intrusion
from ui import draw_zone, draw_box, draw_hud

# Load model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

ZONE = (200, 100, 450, 350)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    intrusion_detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label != "person":
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            bbox = (x1, y1, x2, y2)

            is_anomaly = check_intrusion(bbox, ZONE)

            if is_anomaly:
                intrusion_detected = True

            draw_box(frame, bbox, label, is_anomaly)

    draw_zone(frame, ZONE)
    draw_hud(frame, intrusion_detected)

    cv2.imshow("Iron Man Anomaly Detector", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
