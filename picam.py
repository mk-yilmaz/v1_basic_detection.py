from picamzero import Camera
import time
import cv2

# Kamera-Objekt erstellen
cam = Camera()
# Kurze Pause für die Belichtung
time.sleep(2)


# Gesichtserkennungs-Datei laden (Haarcascade)
xml_datei = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(xml_datei)


# Prüfen, ob die Datei korrekt geladen wurde
if face_cascade.empty():
    print("Fehler: Gesichtserkennung konnte nicht geladen werden!")
    exit()

#Endlosschleife: Kamera prüft ständig auf Gesichter
while True:

    # Temporären Dateinamen festlegen
    temp_filename = "/home/admin/Desktop/temp.jpg"

    # Foto mit der Kamera aufnehmen
    cam.take_photo(temp_filename)

    # Bild mit OpenCV laden 
    img = cv2.imread(temp_filename)

    # Falls Bild nicht geladen werden konnte → überspringen
    if img is None:
        print("Bild konnte nicht geladen werden")
        continue

    # Bild in Graustufen umwandeln (einfachere Verarbeitung)
    grau = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Kontrast verbessern für bessere Gesichtserkennung
    grau = cv2.equalizeHist(grau)
    
    
    # Gesichtserkennung durchführen
    faces = face_cascade.detectMultiScale(grau,scaleFactor=1.1,# Genauigkeit der Suche
                                          minNeighbors=7,# Wie streng es erkannt wird
                                          minSize= (90, 90)) #Mindestgröße eines Gesichts

    # Wenn mindestens ein Gesicht erkannt wurde
    if len(faces) > 0:
        print("Gesicht erkennt!")

        # Dateiname mit Zeitstempel erstellen
        filename = f"/home/admin/Desktop/Picture_{int(time.time())}.jpg"

        # Bild speichern
        cv2.imwrite(filename, grau)

        print (f"Foto gespeichert unter: {filename}")

        # Schleife beenden
        break
    else:
        # Wenn kein Gesicht erkannt wurde → erneut versuchen
        print("Kein Gesicht erkannt...")
        time.sleep(1)
        



# Programm beendet
print("Porgramm beendet")
