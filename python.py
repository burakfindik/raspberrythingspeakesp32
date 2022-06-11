#Thonny IDE'ye yuklenecek kod.
import serial
from urllib.request import urlopen
import time
key = "xxxxxxxxxxxxxxxxx"  # Buraya API anahtarını yazınız.
URL = "https://api.thingspeak.com/update?api_key={}".format(key)



if __name__=='__main__':
    ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
             line =ser.readline().decode('utf-8').rstrip()
             print(line)
             thingspeakHttp = URL + "&field3={}".format(line)
             conn = urlopen(thingspeakHttp)
             time.sleep(1)
             print("\nThingSpeak.com'a gönderildi.")
