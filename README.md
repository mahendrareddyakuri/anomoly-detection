# AI-Based Anomaly Detection System using Object Detection (Jetson)

##  Project Overview

This project is a real-time **AI-based anomaly detection system** built using computer vision on NVIDIA Jetson.

It detects objects from a live camera feed and triggers an alert when a **person enters a restricted zone**.  
The system also includes a futuristic HUD-style interface for visualization.

---

## Objective

To build a real-time intelligent surveillance system that:
- Detects objects using deep learning
- Identifies anomalies based on spatial rules (restricted zone)
- Displays results using a custom UI overlay

---

## Definition of Anomaly

In this project:

> An **anomaly** is defined as a *person entering a predefined restricted zone* in the camera frame.

When this occurs, the system highlights it as an alert event.

---

## Technology Used

- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- NVIDIA Jetson Platform  

---

##  Object Detection Model

We use:

👉 :contentReference[oaicite:0]{index=0}

YOLOv8 is a fast and accurate real-time object detection model that identifies objects such as people, vehicles, etc.

---

##  UI Design

The interface is designed like a futuristic security dashboard (HUD-style).

It includes:
- Real-time detection boxes
- Restricted zone overlay
- System status display
- Anomaly alerts

The UI is inspired by high-tech fictional systems such as:
:contentReference[oaicite:1]{index=1}

---
---

## How It Works

1. Camera captures live video feed  
2. YOLOv8 detects objects in each frame  
3. System checks if a person is inside the restricted zone  
4. If yes → anomaly is triggered  
5. UI displays:
   - Bounding boxes
   - Zone boundary
   - “ANOMALY DETECTED” alert  

---


### Step 1: Install dependencies
pip install -r requirements.txt
<img width="1600" height="1039" alt="WhatsApp Image 2026-04-22 at 12 09 34 AM" src="https://github.com/user-attachments/assets/c98be38b-84a5-4875-810d-2305aac665d1" />
<img width="1600" height="1513" alt="WhatsApp Image 2026-04-22 at 12 09 19 AM" src="https://github.com/user-attachments/assets/c84113de-06fc-4dfd-9c1a-f953c20c90db" />


