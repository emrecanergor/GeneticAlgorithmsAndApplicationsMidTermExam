# GeneticAlgorithmsAndApplicationsMidTermExam
Variable Neighborhood Search Alghoritm and Knapsack Problem with dataset 

#Değişken Mahalle Araması Algoritması
Arama içerisinde kullanılan komşuluğun sistematik olarak değiştirilmesini hedefler. Prensip olarak arama yaparken yerel minimuma rastlandığında komşuluk yapısının değişmesi gerekir. Tüm komşuluk yapısına göre global minimum değeri, yerel olarak optimum düzeydedir. Birkaç komşunun birbirine göre yerel minimumlar değerleri yakın değerlerdir. Mahalle içerisindeki yerel minimum, bir diğer mahalle için minimum değer olmak zorunda değildir. 

#Sırt Çantası Problemi
Problem bir kombinatorik optimizasyon çeşitidir. Belirli bir taşıma kapasitesi olan çantaya koyulacak olan eşyaları, değerine göre sıralamak ve kapasiteyi aşmayacak sekilde değerli eşyaları içerisinde optimum biçimde koymaktır.  Burada çanta içerisinde koyulacak ve koyulmayacak nesneleri 0 ve 1 ile tanımlıyoruz.

“Sırt Çantası Problemi” bir kombinatorik optimizasyon olarak tanımlanır ve “Değişken Mahalle Araması Algoritması” da bu kombinatorik optimizasyon konusuna çözüm getirdiği için birbiriyle eşleşen sorun ve çözüm ikilisidir.

#Kod Analizi
Kodumun içerisinde 5 adet class bulunmaktadır.
Classlar sırası ile şu işlemleri gerçekleştirmektedir:
Evaluate.py -> Knapsack problem için hesaplama yapan sınıftır.
InitSol.py -> Çözüm noktalarını yaratan sınıftır.
NeighborHood.py -> Neighborhood algoritmasının fonksiyonlarını barındıran sınıftır.
StoppingCriteria.py -> Programın iterasyon sayısının verildiği ve kontrol edildiği sınıftır.
Variable_neighborhood.py ->  Problemin çözülmesi için nesnelerin yaratılıp, değerlerin verildiği ve kullanıldığı sınıftır.

#Kod Akışı:
##Variable_neighborhood.py dosyası içerisinde gerçekleşen olaylar, sırasıyla şu şekildedir:
•	Değerler, ağırlıklar, max ağırlık tanımlanır.
•	Kullanılacak olan sınıf nesneleri yaratılır.
•	Noktalar arası hesaplama yapılabilmesi için geçici ve esas değişkenler yaratılır.
•	Sırasıyla Komşuluk arama algoritması için bir yapı kurulur ve her bir fonksiyonuna gönderilir.
•	Stop sınıfı iterasyon sayısını tamamlayana kadar kod dönmeye devam eder.

##Neighborhood.py dosyası içerisinde kullanılan fonksiyonların görevini şu sekilde tanımlayabiliriz:
•	One_flip_nbor -> Tüm değerleri ters çevirir ve mahalle listesine ekler
•	M_flip_nbor -> İki biti birden çevirir.
•	One_m_flip_nbor -> önce one flip yapılır, sonra m kadar daha çevirilir.
•	Sad_nbor:
1.	Rastgele seçimli 3 işleme bağlıdır => 1) swap, 2) add, 3) delete
2.	Rastgele seçilen 2 konumun birbiri ile içerikleri takas edilir
3.	Rastgele seçilen bir nesne eklenir
4.	Rastgele seçilen bir nesne silinir
