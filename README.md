# 🚀 Vision Forge  
### Real-Time Face Emotion Detection using Computer Vision and Embedded Systems  
**Author:** Shazmeen Siddiqui  
**Repository:** vision_forge  

---

## 📌 Project Overview  

*I started with line-follower cars and IR sensors… and somehow ended up teaching a camera how to understand emotions.*

Vision Forge is a **real-time facial emotion detection system** that combines **Python-based computer vision** with **Arduino-driven hardware output**. The system detects **smile** and **sad** expressions from a live camera feed and displays emotion counts on a **16×2 I2C LCD**.

Although the technology stack looks different from traditional IoT, the underlying engineering challenges are the same:  
noisy data, unstable signals, and the need for filtering before meaningful decisions can be made.

This project connects my background in **Arduino-based sensing** with **modern AI-powered vision**, creating a hybrid system that behaves like a physical sensor but sees through a camera.

---

## 🧠 Engineering Problem  

A webcam processes **30+ frames per second**.  
If emotions were counted on every frame, the values would spike unrealistically — just like noisy IR or ultrasonic sensors.

To solve this, Vision Forge implements a **temporal stability filter**:

> An emotion must remain consistent across multiple consecutive frames before it is counted.

This converts noisy video data into **reliable digital events**, exactly how embedded systems handle sensor noise.

---

## ⚙️ System Architecture  

```

Camera
↓
MediaPipe Face Mesh
↓
Mouth Geometry Analysis
↓
Temporal Stability Filter
↓
Structured Serial Data (S:x, D:y)
↓
Arduino UNO
↓
I2C LCD (Custom Emoji Display)

```

---

## 😊 Emotion Detection  

The system tracks two facial landmarks on the mouth and calculates the distance between them:

- Larger distance → **Smile**
- Smaller distance → **Sad**

This is a **geometry-based classifier**, not a black-box neural network, making it transparent, tunable, and efficient.

---

## 🧯 Stability Filtering  

Instead of reacting to every frame, Vision Forge waits for an emotion to remain stable across multiple frames before updating the count.  
This is equivalent to **debouncing a button** or **low-pass filtering a sensor** in electronics.

The result is smooth, realistic emotion tracking.

---

## 🔗 Serial Communication  

Instead of sending single characters, a **structured serial format** is used:

```

S:<smile_count>,D:<sad_count>

```

Example:
```

S:12,D:7

```

This format is:
- Easy to parse
- Scalable
- Reliable
- Ready for cloud or IoT integration

---

## 📟 LCD Emoji Rendering  

I2C LCDs do **not support Unicode emojis**, so Vision Forge manually creates smile and sad icons using the LCD’s **CGRAM memory**.

Each emoji is built from **5×8 pixel patterns** and stored in the LCD’s limited custom character slots — a true embedded-graphics challenge.

---

## 🛠 Technologies Used  

| Layer | Tools |
|------|------|
| Vision | OpenCV, MediaPipe |
| Programming | Python |
| Hardware | Arduino UNO |
| Display | 16×2 I2C LCD |
| Communication | Serial UART |
| Graphics | Custom CGRAM Characters |

---

## 📂 Repository Structure  

```

vision_forge/
├── emotion.py
├── media_test.py
├── lcd_face.ino
└── README.md

```

---

## 🚀 Why This Project Matters  

Vision Forge proves that **computer vision behaves like a real sensor**:

| Embedded Sensors | Vision System |
|-----------------|---------------|
| Noisy readings | Landmark jitter |
| Debouncing | Stability filtering |
| UART packets | Structured serial data |
| LCD pixels | CGRAM emojis |

This mindset allows vision to be deployed in **real embedded systems**, not just software demos.

---

## 🔮 Future Improvements  

- Face-size normalization  
- Confidence-weighted emotion scoring  
- Multi-face detection  
- Cloud logging (IoT integration)  
- Dataset recording for ML training  

---

## 👤 Author  

**Shazmeen Siddiqui**  
B.Tech Engineering Student  
Jamia Millia Islamia
