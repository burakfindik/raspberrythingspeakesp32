# HAVA KALİTESİ ÖLÇÜMÜ VE NESNELERİN İNTERNETİ UYGULAMASI
## Raspberry Pi4 ve ESP32s kullanarak ThingSpeak.com'a veri gönderme ve alarm oluşturma

Raspberry Pi4 ile programlama işlemlerine başlamadan önce aşağıdaki komutlar ile mevcut sürümü güncellememiz gerekmektedir.

`sudo apt-get update` </br>
`sudo apt-get upgrade`

Güncelleme işlemlerini yaptıktan sonra Raspberry Pi4 cihazımıza Arduino IDE'nin mevcut sürümünü kurmamız gerekmektedir.Raspberry Pi4 için **Linux 32bit-ARM** versiyonu indirmemiz gerekmektedir.
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_2.png" width="800" height="500">

Kurulum dosyasını downloads dosyasına indirdikten sonra komut ekranından aşağıdaki komutlar ile kurulumu tamamlamamız gerekmektedir.
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_1.png" width="800" height="500">  
 
Bu işlemle birlikte Raspberry Pi4'e Arduino IDE kurulumu tamamlanıyor.
Arduino IDE ile ESP32s programlayabilmek için aşağıdaki adımları takip edeceğiz.
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_3.png" width="800" height="500">  
  
  

Ek Devre Kartları URL'leri kısmına https://dl.espressif.com/dl/package_esp32_index.json linkini kopyalarak tamam diyoruz.
    
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_4.png" width="400" height="250"> 
  
Kart Yöneticisi kısmından ESP32 yazarak esp32 by espressif systems versiyon 1.0.6'yı IDE'mize kuruyoruz.
  
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_5.png" width="600" height="350"> 
 
Böylelikle Arduino IDE'mize tanımlı olan Nodemcu-32s kartını seçebiliriz.
  
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_6.png" width="600" height="350">   
  
**Raspberry Pi4 ile ESP32 SERİ HABERLEŞME YÖNTEMİ**
  

<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_7.png" width="600" height="500"> 
  
ESP32s'i Raspberry Pi4'ün herhangi bir USB portuna bağlayarak seri bağlantımızı sağlamış oluyoruz.

Seri olarak bağladıktan sonra [ESP32s Kodu ile](https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/ESP32s) Arduino IDE'den ESP32'yi programlıyoruz.

Bu işlemden sonra Raspberry Pi4'te kurulu olan bir Python derleyecisinden (Thonny IDE vs.) [Python Kodu ile](https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/python.py) Raspberry Pi4'ü programlıyoruz.
 
**ThingSpeak.com üzerinde gerekli ayarların yapılması**
 <p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_8.png" width="1000" height="750">
  
 Yukarıdaki resimde gösterildiği gibi proje ismini, açıklamasını yazıp ve kanal aktivasyonlarını yaptıktan sonra konfigirasyonu kaydediyoruz.
 Böylelikle gerekli parametleri kodların içine yazarak ThingSpeak.com'a veri göndermeye başlayabiliriz.
  
 <p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_9.png" width="1000" height="750">
  
Veriler Thingspeak.com üzeriinde MATLAB / Mathwork altyapısını kullarak grafiksel olarak gösteriliyor.
  
Son olarak veriler eğer ayarladığımız aralığın dışına çıkarsa **REACT** oluşturarak mail ile bilgilendirilmeyi sağlıyoruz.
  
  
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_10.png" width="400" height="600">
 
Parametleri belirledikten sonra **save** butonuna tıklıyoruz.[Matlab Kodu ile](https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/matlab_analysis)
Matlab Analysis kısmını programlıyoruz.
<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_11.png" width="600" height="500">

 **Save and Run** butonuna bastığımızda veriler belirttiğimiz aralığın dışına çıkarsa Thingspeak.com'a kaydolduğumuz e-posta hesabına bilgilendirme maili gönderelicektir.

<p align=center>
<img src= "https://github.com/burakfindik/raspberrythingspeakesp32/blob/main/Images/Screenshot_12.png" width="1050" height="700">
 
Thingspeak.com her 30 dakika içersinde 2 defa mail ile bilgilendirme sağlamaktadır.
 
