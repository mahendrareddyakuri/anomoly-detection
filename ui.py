import cv2

def draw_zone(frame, zone):
    cv2.rectangle(frame, (zone[0], zone[1]),
                  (zone[2], zone[3]), (0, 140, 255), 2)


def draw_box(frame, box, label, is_anomaly):
    x1, y1, x2, y2 = box

    if is_anomaly:
        color = (0, 0, 255)
        text = "INTRUSION"
    else:
        color = (0, 255, 0)
        text = label

    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
    cv2.putText(frame, text, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)


def draw_hud(frame, intrusion_detected):
    cv2.putText(frame, "ANOMALY DETECTION",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 140, 255), 2)

    if intrusion_detected:
        cv2.putText(frame, "ANOMALY DETECTED",
                    (140, 60), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)

    # HUD lines
    cv2.line(frame, (0, 80), (640, 80), (0,140,255), 1)
    cv2.line(frame, (0, 400), (640, 400), (0,140,255), 1)
