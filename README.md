# Alarm Sistemi Yazılımı
Bu projede genel olarak kameradan okunan veri üzeriden anlık resimler alınır. Bu resimler python dilinin OpenCV kütüphanesi kullanılarak bazı işlemlere tabi tutulur. Bu işlemlerin temelinde arka planı silmek yatıyor. Bu yöntem ile elde edilen resimdeki eşik değeri ile kameranın başlangıçta hesaplanan eşik değeri arasında karşılaştırma yapılarak hareket olup olmadığı tespit edilmeye çalışılır. Hareket olduğu tespit edildiği zaman bunları kayıt altına alıp kameradan yeni değerler okuyarak sürekli bu işlemler tekrar edilir.

Kamera eşik değeri hesaplayarak karıncalanma olan kameralara optimize etmeyi hedefledim.

NOT : Bu projede kullanılan OpenCV sürümü 3.3'tür.
