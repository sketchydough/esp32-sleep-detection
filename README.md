ESP32-CAM Sleep Detection System

Project Overview

This project demonstrates a simple embedded system that detects eye closure in real-time using an ESP32-CAM. The system processes images locally on the microcontroller and triggers a hardware alert via an LED when the eyes appear closed. The project is designed as a proof-of-concept for edge computing applications in embedded vision systems.

Hardware Requirements:
-ESP32-CAM module (AI Thinker)
-External LED connected to GPIO 12
-USB-to-TTL programmer for uploading code
-Jumper wires for connections

Working Principle:
The ESP32-CAM captures grayscale images from its onboard camera. A fixed rectangular region corresponding to the approximate upper face / eye area is cropped from the image. The system calculates the average brightness of this region. If the brightness falls below a predefined threshold, the LED connected to GPIO 12 is switched ON, indicating that the eyes are closed. Otherwise, the LED remains OFF. This simple brightness-based detection acts as a proxy for eye closure and provides a real-time hardware alert. This method is designed for demonstration purposes and works reliably under controlled lighting conditions. Future improvements can include adaptive thresholds or TinyML-based classifiers for more robust detection.

Notes:
The project is fully embedded and does not require any cloud services or external processing.
The brightness-based method is simple and suitable for proof-of-concept demonstrations.
This project demonstrates embedded image processing, real-time hardware control, and microcontroller-based edge computing.

Future Improvements:
Implement adaptive thresholding to account for varying ambient lighting conditions
Integrate TinyML-based classifier to detect eye open/closed states more reliably
Add additional alert mechanisms such as buzzers or wireless notifications
Expand the detection to continuous drowsiness monitoring.

Setup Instructions:
Connect the ESP32-CAM to the USB-TTL programmer:
TX → U0R
RX → U0T
GND → GND
5V → 5V
IO0 → GND during upload only
Open Arduino IDE and select the following:
Board: AI Thinker ESP32-CAM
Port: the COM port corresponding to your USB-TTL adapter
Upload the sleep_detection.ino sketch.
After uploading, remove IO0 from GND and press the RESET button on the ESP32-CAM.
Observe the LED responding to eye closure. Optionally, open the Serial Monitor (baud rate 115200) to view debug output.
