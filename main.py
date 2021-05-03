import cv2
from datetime import datetime
import os

def resimDegeri(t0,t1,t2):
    fark1=cv2.absdiff(t2,t1)
    fark2=cv2.absdiff(t1,t0)
    return cv2.bitwise_and(fark1,fark2)

if os.path.isfile('Arkaplan.jpg'):
    os.remove("Arkaplan.jpg")
if not os.path.isdir("Resimler"):
    os.mkdir("Resimler")
if not os.path.isdir("HareketliResimler"):
    os.mkdir("HareketliResimler")
kamera_esik_degeri = 0
kamera = cv2.VideoCapture(0)
t0 = cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t1 = cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t2 = cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
ilk_deger = cv2.countNonZero(resimDegeri(t0,t1,t2))
i=0
while i<500:
    cv2.imshow("Esik Degeri Hesaplaniyor...",kamera.read()[1])
    son_deger = cv2.countNonZero(resimDegeri(t0,t1,t2))
    fark_deger = son_deger-ilk_deger
    if fark_deger<0:
        fark_deger=fark_deger*-1
    if fark_deger>kamera_esik_degeri and i>250:
        kamera_esik_degeri=fark_deger
    ilk_deger=son_deger
    t0=t1
    t1=t2
    t2=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    i=i+1
cv2.destroyWindow("Esik Degeri Hesaplaniyor...")
zamanKontrol = datetime.now().strftime('%Ss')
print("Eşik Değeriniz : "+(str)(kamera_esik_degeri)+" olarak hesaplanmıştır.")
arkaplan = kamera.read()[1]
cv2.imwrite('Arkaplan.jpg',arkaplan)
print("Arkaplan başarı ile kayıt edilmiştir.")
i=1
while True:
    cv2.imshow("EYazilim Alarm Sistemi.",kamera.read()[1])
    resimOlustu = resimDegeri(t0,t1,t2)
    son_deger = cv2.countNonZero(resimOlustu)
    fark_deger = son_deger-ilk_deger
    if fark_deger<0:
        fark_deger=fark_deger*-1
    if fark_deger>kamera_esik_degeri and zamanKontrol != datetime.now().strftime('%Ss'):
        fark_resim=kamera.read()[1]
        hareketli_alan=cv2.absdiff(arkaplan,fark_resim)
        cv2.imwrite('Resimler/'+datetime.now().strftime('%m%d_%Hh%Mm%Ss%f')+'.jpg',fark_resim)
        cv2.imwrite('HareketliResimler/'+datetime.now().strftime('%m%d_%Hh%Mm%Ss%f')+'.jpg',hareketli_alan)
        print((str)(i)+". resim kayıt edildi.")
        i = i+1
    zamanKontrol = datetime.now().strftime('%Ss')
    ilk_deger = son_deger
    t0 = t1
    t1=t2
    t2=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    key = cv2.waitKey(10)
    if key ==27:
        cv2.destroyAllWindows()
        break
