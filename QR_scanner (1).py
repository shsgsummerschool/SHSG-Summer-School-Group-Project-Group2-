#Gebaut mit folgendem Tutorial: https://www.youtube.com/watch?v=IOhZqmSrjlE
# installiert werden muss: pip install opencv-python, pyzbar

import cv2 #read Image / Camera Input
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0) 
cap.set (3,640) #3 - width of the frame
cap.set (4,480) #4 - Height

def scan_QR_code ():
    print ("Do you want to scan a QR Code?")
    answer = input()
    if answer == "yes":
        camera = True  #mit Button verknüpfen --> scan QR Code --> dann settet der Button die Camera auf = true
        while camera == True:
            success, frame = cap.read()

            for code in decode(frame):
                x = code.data.decode("utf-8")
                return x  #@massimo -> hier müssen wir es irgendwie schaffen, dass man auf diese Variable dann auch global zugreifen kann um sie weiter zu verwenden. Zudem gibts im Terminal no eine WARN:0 Fehlermeldung
              
            cv2.imshow("Testing-code-scan", frame) # definition of the Camera Window where the code can be scanned
            cv2.waitKey(1)


l = print(scan_QR_code()) #l beinhaltet die Funktion, die die Medikamenteninfos liest und printed

#gem. Video Kommentar: x = code.data.decode('utf-8') #--> sollte gescannte info als variable x speichern