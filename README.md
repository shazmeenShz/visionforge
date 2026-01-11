# Vision Forge

<div align="center">

**Real-Time Facial Emotion Detection with Embedded Systems Integration**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Arduino](https://img.shields.io/badge/Arduino-UNO-00979D.svg)](https://www.arduino.cc/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*Bridging computer vision and embedded systems through intelligent emotion recognition*

[Features](#-key-features) • [Architecture](#-system-architecture) • [Technology](#-technology-stack) • [Installation](#-installation) • [Usage](#-usage)

</div>

---

## 🎯 Overview

Vision Forge represents the convergence of **computer vision** and **embedded systems engineering**, demonstrating that visual data can be processed with the same rigor as traditional sensor inputs. This system performs real-time facial emotion detection, translating high-frequency video streams into reliable digital events displayed on physical hardware.

Starting from fundamental robotics with line-follower systems and IR sensors, this project evolved into a sophisticated vision-based sensing platform that treats camera input as a high-dimensional sensor requiring intelligent filtering and processing.

### The Core Challenge

Modern webcams generate 30+ frames per second, creating a flood of visual data. Without proper signal processing, emotion detection becomes erratic—analogous to reading unfiltered noise from an ultrasonic sensor. Vision Forge solves this through **temporal stability filtering**, ensuring only persistent emotional states trigger system updates.

---

## ✨ Key Features

- **Real-time facial landmark detection** using MediaPipe's Face Mesh
- **Geometry-based emotion classification** (transparent, tunable, efficient)
- **Temporal stability filtering** for noise-resistant recognition
- **Structured serial communication** protocol for reliable data transmission
- **Custom LCD emoji rendering** via CGRAM programming
- **Hardware-software integration** bridging Python and Arduino ecosystems

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     VISION PROCESSING                        │
├─────────────────────────────────────────────────────────────┤
│  Camera Feed (30 fps)                                        │
│           ↓                                                  │
│  MediaPipe Face Mesh (468 landmarks)                         │
│           ↓                                                  │
│  Mouth Geometry Analysis                                     │
│           ↓                                                  │
│  Temporal Stability Filter                                   │
│           ↓                                                  │
│  Event Generator                                             │
└─────────────────────────────────────────────────────────────┘
                         ↓
              Serial Protocol: S:x,D:y
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                   EMBEDDED HARDWARE                          │
├─────────────────────────────────────────────────────────────┤
│  Arduino UNO (UART Receiver)                                 │
│           ↓                                                  │
│  Data Parser & Validator                                     │
│           ↓                                                  │
│  I2C Communication                                           │
│           ↓                                                  │
│  16×2 LCD Display (Custom CGRAM Characters)                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Technical Deep Dive

### Emotion Detection Algorithm

Vision Forge employs a **geometry-based classification approach** rather than black-box neural networks, providing interpretability and efficiency:

```python
# Facial landmark analysis
mouth_height = calculate_distance(upper_lip, lower_lip)

if mouth_height > SMILE_THRESHOLD:
    emotion = "SMILE"
elif mouth_height < SAD_THRESHOLD:
    emotion = "SAD"
```

**Advantages:**
- Transparent decision-making process
- Real-time performance on standard hardware
- Easy threshold tuning for different use cases
- No training data required

### Temporal Stability Filter

Inspired by embedded systems signal processing, this filter prevents spurious detections:

```python
def is_stable(emotion, history, required_frames=5):
    """
    Debounce facial expressions across temporal window
    Similar to debouncing mechanical switches
    """
    return all(frame == emotion for frame in history[-required_frames:])
```

This approach converts noisy visual data into **reliable digital events**, mirroring how embedded systems handle sensor debouncing and low-pass filtering.

### Serial Communication Protocol

A structured data format ensures reliable hardware communication:

```
Format: S:<smile_count>,D:<sad_count>\n
Example: S:42,D:13\n
```

**Protocol Benefits:**
- Self-descriptive data structure
- Easy parsing with simple string operations
- Extensible for additional emotion types
- Compatible with IoT platforms and cloud logging

### Custom LCD Graphics

Standard I2C LCDs lack Unicode support, requiring manual character creation using the LCD's CGRAM (Character Generator RAM):

```cpp
// 5×8 pixel matrix defining smile emoji
byte smile[8] = {
  0b00000,
  0b01010,
  0b01010,
  0b00000,
  0b10001,
  0b01110,
  0b00000,
  0b00000
};
lcd.createChar(0, smile);
```

This showcases low-level graphics programming in resource-constrained environments—a fundamental embedded systems skill.

---

## 💻 Technology Stack

| **Layer**          | **Technology**                          |
|--------------------|-----------------------------------------|
| Computer Vision    | OpenCV, MediaPipe Face Mesh             |
| Language           | Python 3.8+                             |
| Microcontroller    | Arduino UNO (ATmega328P)                |
| Display            | 16×2 I2C LCD (HD44780)                  |
| Communication      | UART Serial (9600 baud)                 |
| Custom Graphics    | LCD CGRAM Programming                   |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Arduino IDE
- USB cable for Arduino connection

### Python Environment Setup

```bash
# Clone repository
git clone https://github.com/yourusername/vision_forge.git
cd vision_forge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install opencv-python mediapipe pyserial numpy
```

### Arduino Setup

1. Open `lcd_face.ino` in Arduino IDE
2. Install required library: `LiquidCrystal_I2C`
3. Configure I2C address if needed (default: 0x27)
4. Upload to Arduino UNO

### Hardware Connections

```
Arduino UNO ←→ I2C LCD
  5V        →   VCC
  GND       →   GND
  A4 (SDA)  →   SDA
  A5 (SCL)  →   SCL
```

---

## 🚀 Usage

1. **Connect hardware:**
   - Attach I2C LCD to Arduino
   - Connect Arduino to computer via USB

2. **Identify serial port:**
   ```bash
   # Linux/Mac
   ls /dev/tty.*
   
   # Windows
   # Check Device Manager → Ports (COM & LPT)
   ```

3. **Update serial port in `emotion.py`:**
   ```python
   ser = serial.Serial('COM3', 9600)  # Change to your port
   ```

4. **Run the system:**
   ```bash
   python emotion.py
   ```

5. **Test MediaPipe (optional):**
   ```bash
   python media_test.py
   ```

---

## 📊 Performance Metrics

- **Frame Processing Rate:** 30 fps on standard webcam
- **Detection Latency:** < 50ms per frame
- **Stability Window:** 5 frames (~167ms at 30fps)
- **Serial Baud Rate:** 9600 bps
- **LCD Update Rate:** ~200ms per refresh

---

## 🧩 Project Structure

```
vision_forge/
│
├── emotion.py          # Main emotion detection system
├── media_test.py       # MediaPipe testing utility
├── lcd_face.ino        # Arduino firmware for LCD control
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

---

## 🔄 Design Philosophy

Vision Forge demonstrates that **computer vision systems share fundamental characteristics with traditional embedded sensors:**

| **Embedded Sensors**     | **Vision System**              |
|--------------------------|--------------------------------|
| Noisy analog readings    | Landmark position jitter       |
| Hardware debouncing      | Temporal stability filtering   |
| Structured UART packets  | Serialized emotion data        |
| LCD pixel manipulation   | CGRAM custom characters        |
| Real-time constraints    | 30 fps processing requirement  |

This unified perspective enables vision systems to be deployed as **first-class sensors** in embedded applications, not merely software demonstrations.

---

## 🔮 Future Roadmap

- [ ] **Face-size normalization** for distance-independent detection
- [ ] **Confidence scoring** with weighted temporal averaging
- [ ] **Multi-face tracking** for group emotion analysis
- [ ] **Cloud integration** for IoT-enabled emotion logging
- [ ] **Dataset collection** for machine learning augmentation
- [ ] **Additional emotions** (anger, surprise, neutral)
- [ ] **ESP32 port** for wireless operation
- [ ] **OLED display** support with higher resolution graphics

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss proposed modifications.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Shazmeen Siddiqui**  
B.Tech Engineering Student  
Jamia Millia Islamia

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/yourprofile)

---

<div align="center">

**If you found this project interesting, please consider giving it a ⭐**

*Built with curiosity, powered by engineering*

</div>
