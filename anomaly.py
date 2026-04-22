# anomaly.py

def check_intrusion(box, zone):
    x1, y1, x2, y2 = box

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    if zone[0] < cx < zone[2] and zone[1] < cy < zone[3]:
        return True
    return False
