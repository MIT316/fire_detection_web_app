# import cv2        
# import pygame
# import requests  # Flask API Call ke liye

# # Initialize pygame mixer for playing sound
# pygame.init()
# pygame.mixer.init()

# fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml') 
# vid = cv2.VideoCapture(0) 

# def play_alarm_sound():
#     pygame.mixer.music.load("mixkit-emergency-alert-alarm-1007.wav")
#     pygame.mixer.music.play()

# while True:
#     ret, frame = vid.read() 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
#     fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

#     for (x, y, w, h) in fire:
#         cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
#         cv2.putText(frame, "Fire Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]

#         print("🔥 Fire detected! Sending alert to website...")
        
#         # 🔥 **Flask API ko call karna**
#         try:
#             requests.get("http://127.0.0.1:5000/fire_detected")  # Flask API Call
#         except requests.exceptions.RequestException as e:
#             print("Error sending alert:", e)
        
#         play_alarm_sound()

#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  
#         break

# vid.release()
# cv2.destroyAllWindows()


# import cv2
# import requests
# import pygame
# import time

# # Load fire detection model
# fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

# # Initialize webcam
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use CAP_DSHOW for Windows

# # Initialize Pygame for alert sound
# pygame.init()
# pygame.mixer.init()

# def play_alarm_sound():
#     """Play fire alert sound."""
#     pygame.mixer.music.load("mixkit-emergency-alert-alarm-1007.wav")
#     pygame.mixer.music.play()

# def get_location():
#     """Get system's location using Google's Geolocation API."""
#     GEOLOCATION_API_KEY = "AIzaSyA4cu1uYO9RyxposmyaAUbpuEwBWJNkqrE"  # Replace with your API key
#     try:
#         response = requests.post(f"https://www.googleapis.com/geolocation/v1/geolocate?key={GEOLOCATION_API_KEY}", json={})
#         data = response.json()
#         lat = data.get("location", {}).get("lat")
#         lon = data.get("location", {}).get("lng")
#         return lat, lon
#     except requests.exceptions.RequestException as e:
#         print("Error fetching location:", e)
#         return None, None

# def detect_fire():
#     """Detect fire and send alert to Flask server."""
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

#         fire_detected = False  # Flag to track fire detection

#         for (x, y, w, h) in fire:
#             cv2.rectangle(frame, (x-20, y-20), (x+w+20, y+h+20), (255, 0, 0), 2)
#             cv2.putText(frame, "Fire Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
#             fire_detected = True  # Fire detected
#             lat, lon = get_location()  # Get current location
            
#             print(f"🔥 Fire detected at location: {lat}, {lon}")

#             # Send fire alert to Flask app
#             try:
#                 response = requests.get(f"http://127.0.0.1:5000/fire_detected?lat={lat}&lon={lon}")
#                 print("🔥 Alert sent to server:", response.text)
#             except requests.exceptions.RequestException as e:
#                 print("Error sending alert:", e)

#             # Play alarm sound
#             play_alarm_sound()
#             time.sleep(5)  # Avoid sending alerts too frequently

#         cv2.imshow("Fire Detection", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# detect_fire()

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import requests
# import geocoder  # To get real-time location
# import time

# # Use the correct file path
# cascade_path = r"C:\Users\Mith\OneDrive\Desktop\REAL-TIME-FIRE-DETECTION\fire_detection_cascade_model.xml"

# # Load the cascade classifier
# fire_cascade = cv2.CascadeClassifier(cascade_path)

# # Check if the file loaded correctly
# if fire_cascade.empty():
#     print("❌ Error: Unable to load fire_detection_cascade_model.xml. Check the file path!")
#     exit()  # Stop execution if the file is missing

# # Start capturing video
# cap = cv2.VideoCapture(0)  # Use 0 for webcam

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ Error: Could not read frame from webcam.")
#         break

#     # Convert frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect fire
#     fires = fire_cascade.detectMultiScale(gray, 1.2, 5)

#     for (x, y, w, h) in fires:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
#         cv2.putText(frame, "🔥 FIRE DETECTED!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

#         # Get real-time location
#         g = geocoder.ip('me')
#         if g.latlng:
#             lat, lon = g.latlng
#         else:
#             lat, lon = None, None
#             print("⚠️ Warning: Could not retrieve location!")

#         # Send fire alert to Flask server
#         if lat and lon:
#             try:
#                 response = requests.get(f'http://127.0.0.1:5000/fire_detected?lat={lat}&lon={lon}')
#                 if response.status_code == 200:
#                     print(f"🔥 Alert sent to server: {response.json()}")
#                 else:
#                     print(f"⚠️ Server Error: {response.status_code}")
#             except requests.exceptions.RequestException as e:
#                 print("❌ Error sending alert:", e)

#     # Show the video feed
#     cv2.imshow("🔥 Fire Detection System", frame)

#     # Exit on pressing 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




# import cv2
# import base64
# import geocoder
# import socketio

# # Connect to Flask server using WebSockets
# sio = socketio.Client()
# sio.connect("http://127.0.0.1:5005")

# # Load the fire detection model
# fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     fire = fire_cascade.detectMultiScale(gray, 1.2, 5)

#     fire_detected = False
#     for (x, y, w, h) in fire:
#         fire_detected = True
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     # If fire is detected, get location and send alert
#     if fire_detected:
#         location = geocoder.ip("me")
#         if location.latlng:  # Ensure location is available
#             latitude, longitude = location.latlng

#             # Convert image to base64
#             _, buffer = cv2.imencode('.jpg', frame)
#             img_str = base64.b64encode(buffer).decode()

#             # Send fire alert via WebSocket
#             sio.emit("fire_alert", {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "image": img_str
#             })

#     cv2.imshow("Fire Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# sio.connect("http://127.0.0.1:5005")






# import cv2
# import base64
# import geocoder
# import socketio

# # Connect to Flask server using WebSockets
# sio = socketio.Client()
# sio.connect("http://127.0.0.1:5005")

# # Load the fire detection model
# fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     fire = fire_cascade.detectMultiScale(gray, 1.2, 5)

#     fire_detected = False
#     for (x, y, w, h) in fire:
#         fire_detected = True
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     # If fire is detected, get location and send alert
#     if fire_detected:
#         location = geocoder.ip("me")
#         if location.latlng:  # Ensure location is available
#             latitude, longitude = location.latlng

#             # Convert image to base64
#             _, buffer = cv2.imencode('.jpg', frame)
#             img_str = base64.b64encode(buffer).decode()

#             # Send fire alert via WebSocket
#             sio.emit("fire_alert", {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "image": img_str
#             })

#     cv2.imshow("Fire Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# sio.connect("http://127.0.0.1:5005")


# import cv2
# import base64
# import geocoder
# import socketio

# # Connect to Flask server using WebSockets
# sio = socketio.Client()
# sio.connect("http://127.0.0.1:5005")

# # Load fire detection model
# fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     fire = fire_cascade.detectMultiScale(gray, 1.2, 5)

#     fire_detected = False
#     for (x, y, w, h) in fire:
#         fire_detected = True
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     if fire_detected:
#         location = geocoder.ip("me")
#         if location.latlng:
#             latitude, longitude = location.latlng
#             _, buffer = cv2.imencode('.jpg', frame)
#             img_str = base64.b64encode(buffer).decode()

#             sio.emit("fire_alert", {
#                 "latitude": latitude,
#                 "longitude": longitude,
#                 "image": img_str
#             })

#     cv2.imshow("Fire Detection", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import torch
from ultralytics import YOLO

model = YOLO("my_trained_model.pt")  # Load the pre-trained model

results = model(r"C:\Users\Mith\OneDrive\Desktop\REAL-TIME-FIRE-DETECTION\Copy of vid.mp4")  # Replace with an actual image path
results.show()  # Show the output with bounding boxes
