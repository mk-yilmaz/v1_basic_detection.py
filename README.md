# raspberry-pi-face-detection-opencv
## 🇬🇧 English Version
# Face Detection with Python (Raspberry Pi Camera)
This project demonstrates a simple face detection system using Python and a Raspberry Pi camera.

# Features
- Capturing images using the Raspberry Pi camera
- Face detection using OpenCV (Haar Cascade)
- Automatic image saving when a face is detected
- Timestamp-based file naming

# Requirements
- Python 3.x
- OpenCV (cv2)
- picamzero
- Haarcascade file: `haarcascade_frontalface_default.xml`

# Usage
Install required libraries:
pip install opencv-python picamzero

Make sure the Haarcascade file is in the project directory.

Run the script:
python v1_basic_detection.py

# How it works
- The camera captures images in a loop
- Each image is converted to grayscale
- OpenCV detects faces using Haar Cascades
- If a face is detected, the image is automatically saved and the program stops

# Output
Saved images are stored in:
`/home/admin/Desktop/`

# Author
M. Yilmaz


## 🇩🇪 German Version
# Gesichtserkennung mit Python (Raspberry Pi Kamera)
Dieses Projekt zeigt eine einfache Gesichtserkennung mit Python unter Verwendung einer Raspberry Pi Kamera.

# Funktionen
- Aufnahme von Bildern über die Kamera.
- Gesichtserkennung mit OpenCV (Haarcascade).
- Automatisches Speichern eines Bildes bei erkannter Person.
- Verwendung von Zeitstempeln für Dateinamen.

# Voraussetzungen
- Python 3.x
- OpenCV cv2.
- picamzero.
- Haarcascade-Datei:
  haarcascade_frontalface_default.xml

# Verwendung
1. Benötigte Bibliotheken installieren:
3. pip install opencv-python picamzero.
4. Sicherstellen, dass sich die Haarcascade-Datei im Projektordner befindet.
5. Script starten:
6. python v1_basic_detection.py

# Funktionsweise
- Die Kamera nimmt regelmäßig Bilder auf.
- Jedes Bild wird in Graustufen umgewandelt und optimiert.
- OpenCV prüft das Bild auf Gesichter.
- Sobald ein Gesicht erkannt wird, wird das Bild automatisch gespeichert.
Anschließend beendet sich das Programm.

# Ausgabe
Gespeicherte Bilder befinden sich unter:
/home/admin/Desktop/

# Autor
M. Yilmaz


