# v1_basic_detection.py (Version 1)

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

#Autor
M. Yilmaz


