# Alarm Sistemi Yazılımı
Projemde genel olarak kameradan okuduğum veri üzeriden anlık resimler aldım. Bu resimleri python dilinin OpenCV kütüphanesini kullanarak bazı işlemlere tabi tuttum. Bu işlemlerin temelinde arka planı silmek yatıyor. Bu yöntem ile elde edilen resimdeki eşik değeri ile kameranın başlangıçta hesaplanan eşik değeri arasında karşılaştırma yaparak hareket olup olmadığını tespit etmeye çalıştım. Hareket olduğu tespit edildiği zaman bunları kayıt altına alıp kameradan yeni değerler okuyarak sürekli bu işlemlere tabi tutturdum.

Kamera eşik değeri hesaplayarak karıncalanma olan kameralara optimize etmeyi hedefledim.

NOT : Bu projede kullanılan OpenCV sürümü 3.3'tür.
