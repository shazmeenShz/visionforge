import cv2
import mediapipe as mp
import serial
import math
import time

#SERIAL SETUP
#arduino = serial.Serial('COM6', 9600)
time.sleep(2) 

# COUNTERS 
smile_count = 0
sad_count = 0

current_emotion = None
emotion_frames = 0
MIN_FRAMES = 15  

#CAMERA SETUP
webcam = cv2.VideoCapture(0)

#MEDIAPIPE SETUP
mp_face = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

#FACE MESH
with mp_face.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:
        ret, frame = webcam.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        height, width, _ = frame.shape

        detected_emotion = None

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:

#MOUTH LANDMARKS
                p1 = face_landmarks.landmark[306]
                p2 = face_landmarks.landmark[61]

                x1, y1 = int(p1.x * width), int(p1.y * height)
                x2, y2 = int(p2.x * width), int(p2.y * height)

                cv2.circle(frame, (x1, y1), 2, (0, 0, 255), -1)
                cv2.circle(frame, (x2, y2), 2, (0, 0, 255), -1)

                #DISTANCE
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                #EMOTION DETECTION
                if distance > 60:
                    detected_emotion = "SMILE"
                elif distance < 56:
                    detected_emotion = "SAD"

        #STABILITY FILTER 
        if detected_emotion == current_emotion and detected_emotion is not None:
            emotion_frames += 1
        else:
            emotion_frames = 0
            current_emotion = detected_emotion

        #COUNT ONLY ONCE
        if emotion_frames == MIN_FRAMES:
            if current_emotion == "SMILE":
                smile_count += 1
            elif current_emotion == "SAD":
                sad_count += 1

        #SEND TO ARDUINO
        #data = f"S:{smile_count},D:{sad_count}\n"
        #arduino.write(data.encode())

        #DISPLAY INFO
        cv2.putText(frame, f"Smile Count: {smile_count}",
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 0), 2)

        cv2.putText(frame, f"Sad Count: {sad_count}",
                    (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 0, 255), 2)

        if current_emotion:
            cv2.putText(frame, f"Emotion: {current_emotion}",
                        (20, 120), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 0), 2)

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(10) & 0xFF == 27:
            break
