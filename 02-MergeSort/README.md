# MERGE SHORT (Birleştirmeli Sıralama) ALGORİTMASI

## İçindekiler 
- [Merge Sort Nedir](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-sort-nedir)
- [Algoritma Nasıl Çalışır](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#algoritma-nas%C4%B1l-%C3%A7al%C4%B1%C5%9F%C4%B1r-s%C3%B6zde-kod)
- [Örnek Kod](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#%C3%B6rnek-kod)
- [Örnek Algoritma İncelemesi](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#%C3%B6rnek-algoritma-i%CC%87ncelemesi)
- [En İyi Durum ve En Kötü Durum](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#en-i%CC%87yi-durum-ve-en-k%C3%B6t%C3%BC-durum)
- [Karmaşıklık Hesabı](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#karma%C5%9F%C4%B1kl%C4%B1k-hesab%C4%B1) 
- [Kaynakça](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#kaynak%C3%A7a)
---

 ## Merge Sort Nedir?

Varolan bir diziyi (sıralı-sırasız) belli bir işlem adımları uygulayarak diziyi sıralama işlemidir. Bir böl ve yönet algoritmasıdır. Özyineli bir algoritmadır. En alt dizi iki ögeli olana kadar yarılama işlemi devam eder. Sonra "Merge (Birleştirme)" işlemiyle altdiziler ikişer ikişer bölünüş sırasıyla sıralı olarak bir üst dizide birleştirilir. Süreç sonunda en üstte sıralı diziye ulaşılır.Sıralama yaparken değerleri tek tek kontrol ederek kıyaslama yapar ve sıraya koyar. Bağlı liste sıralamasında seçilebilecek en performanslı algoritma Merge Sort algoritmasıdır. Çünkü bağlı listelerin yapısı gereği mergesort bellekte fazladan sadece 1 birim yer tutar ve bağlı listelerin yavaş ve rastgele erişim performansı nedeniyle quicksort gibi diğer algoritmaların çalışma performansı düşer, Heap Sort gibi algoritmalar için ise imkansızdır.

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-short-birle%C5%9Ftirmeli-s%C4%B1ralama-algori%CC%87tmasi)

 ## Algoritma Nasıl Çalışır (Sözde Kod)

1. Diziyi ortadan ikiye böl
2. En alt dizi iki elemanlı olana kadar bölmeye devam et. 
3. İki elemanlı dizilerin elemanlarını kendi aralarında karşılaştır ve sırala.
4. İki elemanlı sıralı farklı dizileri kendi aralarında sırayla karşılaştırıp sıralayarak birleştir. 
5. Tüm alt diziler birleşene kadar süreci devam ettir.
6. Tek liste halinde bir sıralı dizi elde edilmiş olunur. 
Yukarıdaki gibi işlemler devam eder. 

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-short-birle%C5%9Ftirmeli-s%C4%B1ralama-algori%CC%87tmasi)
## Örnek Kod

>code.py adlı dosyada çözüm sunulmuştur.


### Python Örnek Kod -1
```python
dizi=[89,45,68,90,29,34]
def BirlestirSiralama(dizi):
    if len(dizi) > 1:  # minimum 2 boyutunda olması sağlanıyor
        boyut = len(dizi)//2  # Dizi ikiye bölünüyor
        solDizi = dizi[:boyut] #sol dizi belirleniyor
        sagDizi = dizi[boyut:] #sag dizi belirleniyor
        BirlestirSiralama(solDizi) # altdizi için bölme tekrardan çağrılıyor
        BirlestirSiralama(sagDizi) # altdizi için bölme tekrardan çağrılıyor
        i = j = k = 0 # i indisi sol dizi için j indisi sag dizi için k indisi dizinin kendi indisi için 
        while i < len(solDizi) and j < len(sagDizi): # sol dizi ve sag dizi iceriklerine bakılıyor
            if solDizi[i] < sagDizi[j]: # sol dizi sag dizi icerikleri karşılaştırılıyor
                dizi[k] = solDizi[i]
                i += 1
            else:
                dizi[k] = sagDizi[j]
                j += 1
            k += 1
        while i < len(solDizi): #sol dizinin hepsine bakılmamışsa kalan degerlere alınıyor
            dizi[k] = solDizi[i]
            i += 1
            k += 1
        while j < len(sagDizi): #sağ dizinin hepsine bakılmamışsa kalan degerlere alınıyor
            dizi[k] = sagDizi[j]
            j += 1
            k += 1
print("Sırasız Dizi : \t\t",dizi)
BirlestirSiralama(dizi)
print("Sıralı Dizi  : \t\t",dizi)
```

Örnek Kod 1 Çıktısı:

![img](https://github.com/emre-cakar/Siralama-Algoritmalari/blob/main/01-MergeSort/code.png?raw=true)

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-short-birle%C5%9Ftirmeli-s%C4%B1ralama-algori%CC%87tmasi)

 ## Örnek Algoritma İncelemesi


* Elimizde aşağıdaki gibi bir dizi olduğunu düşünelim. 

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |

---

* Diziden, her seferinden ortadan ikiye bölerek iki alt dizi oluşturulur. Tek yada çift eleman olana kadar altdiziler bölünmeye devam edilir. 

    * Ham diziden **89 45 68 (solDizi)**  - **90 29 34(sagDizi)** şeklinde iki dizi oluşur.
    * 89 45 68 dizisinden **89** ve **45 68** şeklinde iki alt dizi oluşturulur. 
    * 90 29 34 dizisinden **90** ve **29 34** şeklinde iki alt dizi oluşturulur. 
    * Eleman sayısı 2 den büyük bir dizi kalmadığı için bölme işlemi sonlandırılır.
    
    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |----    |----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |:----:  |:----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90    |    29   |   34   |      |       |       |
    | 1. Adım   |   89   |   45   |   68   |    \| \|  |   \| \|    |    90   |   29   |   34   |       |
    | 2. Adım   |   89   |   \| \|    |   45   |   68   |   \| \|    |    90   |    \| \|   |   29   |   34   |

---

* En alt satırda bulunan diziler kendi içinde sıralanır. 
    * **89** dizisi tek elemanlı olduğu için işlem yapılmaz. 
    * **45 68** dizisi sıralı olduğundan işlem yapılmaz.
    * **90** dizisi tek elemanlı olduğundan işlem yapılmaz.
    * **29 34** dizisi sıralı oluduğundan bir işlem yapılmaz. 

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |----    |----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |:----:  |:----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90    |    29   |   34   |      |       |       |
    | 1. Adım   |   89   |   45   |   68   |    \| \|  |   \| \|    |    90   |   29   |   34   |       |
    | 2. Adım   |   89   |   \| \|    |   45   |   68   |   \| \|    |    90   |    \| \|   |   29   |   34   |
---
 
* Kendisinden bölünerek sol ve sağ şeklinde ayrılarak oluşturulan diziler karşılaştırılarak sıralı bir dizi halinde birleştirilir.
    * 2\. adımda bulunan **89** ve **45 68** dizileri karşılaştırılarak birleştirme işlemi yapılır. 
        * **89** değeri **45** değerinden büyük olduğu için yeni dizinin ilk elemanı **45** olur. 
        * **89** değeri **68** değerinden büyük olduğu için yeni dizinin ikinci elamnı **68** olur. 
        * **89** değeri yeni dizinin üçüncü elemanı olur. 
        
        > Sağ dizide eleman kalmadığı için sol dizideki elemanlar direk yazılır (Bir önceki adımda diziler kendi içinde sıralanmıştır. Tekrardan karşılaştırmaya gerek kalmamıştır.)
    * 2\. adımda bulunan **90** ve **29 34** dizileri karşılaştırılarak birleştirme işlemi yapılır. 
        * **90** değeri **29** değerinden büyük olduğu için yeni dizinin ilk elamanı **29** olur.
        * **90** değeri **34** değerinden büyük olduğu için yeni dizinin ikinci elemanı **34** olur.
        * **90** değeri yeni dizinin üçüncü elemanı olur. 
        > Sağ dizide eleman kalmadığı için sol dizideki elemanlar direk yazılır (Bir önceki adımda diziler kendi içinde sıralanmıştır. Tekrardan karşılaştırmaya gerek kalmamıştır.)

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |----    |----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |:----:  |:----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90    |    29   |   34   |      |       |       |
    | 1. Adım   |   89   |   45   |   68   |    \| \|  |   \| \|    |    90   |   29   |   34   |       |
    | 2. Adım   |   89   |   \| \|    |   45   |   68   |   \| \|    |    90   |    \| \|   |   29   |   34   |
    | 3. Adım   |   45   |   68   |   89   |    \| \|  |   \| \|    |    29   |   34   |   90   |
---
    
    
* 3\. adım da oluşan yeni diziler kendi aralarında karşılaştırılarak sıralı bir şekilde birleştirilir. 
    * Sol dizi (**45 68 89**) ve sağ dizi (**29 34 90**) karşılaştırılır. 
    * **45** değeri sağ dizinin ilk elemanından büyük olduğundan yeni dizininin ilk elemanı **29** olur. 
    * **45** değeri sağ dizinin ikinci elemanından büyük olduğundan yeni dizinin ikinci elemanı **34** olur.
    * **45** değeri sağ dizinin üçüncü elemanından küçük olduğundan yeni dizinin üçüncü elemanı **45** olur.
    * **68** değeri sağ dizinin son elemanından küçük olduğundan yeni dizinin dördüncü elamanı **68** olur.
    * **89** değeri sağ dizinin son elemanından küçük olduğundan yeni dizinin dördüncü elamanı **89** olur.
    * Yeni dizinin son elamanı geri kalan **90** değeri olur. 


    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |----    |----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |:----:  |:----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90    |    29   |   34   |      |       |       |
    | 1. Adım   |   89   |   45   |   68   |    \| \|  |   \| \|    |    90   |   29   |   34   |       |
    | 2. Adım   |   89   |   \| \|    |   45   |   68   |   \| \|    |    90   |    \| \|   |   29   |   34   |
    | 3. Adım   |   45   |   68   |   89   |    \| \|  |   \| \|    |    29   |   34   |   90   |
    | 4. Adım   |   29   |   34   |   45   |   68    |    89   |   90   |      |       |       |
---

 ```
 Sıralı Dizi :
29 34 45 68 89 90
 ``` 

![img](https://github.com/emre-cakar/Siralama-Algoritmalari/blob/main/01-InsertionSort/Example.png?raw=true)

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-short-birle%C5%9Ftirmeli-s%C4%B1ralama-algori%CC%87tmasi)

## En İyi Durum ve En Kötü Durum 

**En iyi durum** dizinin **sıralı** olmasıdır.  Karmaşıklığı O(n-1)

**En kötü durum** ise dizinin **ters sıralı** olmasıdır. Karmaşıklığı O(n^2)

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/02-MergeSort#merge-short-birle%C5%9Ftirmeli-s%C4%B1ralama-algori%CC%87tmasi)

## Karmaşıklık Hesabı

Birleştirmeli sıralama algoritmasının zaman karmaşıklığı hesaplanırken, yapılan karşılaştırmalar ve yer değiştirmeler dikkate alınır. Birleştirmeli sıralama algoritması n elemanlı bir listede, her bölüm sonucunda oluşan karşılaştırma n/2-1 , n/4-1 ... vb. şekliden olur. Her adımda ki karşılaştırma sayımız O(n) seviyesinde olur. Peki kaç defa bu adım gerçekleştiriyor? Her aşamada n elamanlı dizi sayısı yarıya iniyor. Bu durumda log2n olmuş olur. Karmaşıklığı ise O(logn) seviyesinde olur. Bu durumda bunları çarptığımızda O(nlogn) şekliden bir karmaşıklık elde etmiş oluruz.

Sonuç n karedir. Bu durumda karmaşıklık: **O(nlogn)**

[![](https://img.youtube.com/vi/Sx1VfR7EvnA/maxresdefault.jpg)](https://youtu.be/Sx1VfR7EvnA)

[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#inserti%CC%87on-short-eklemeli-s%C4%B1ralama-algori%CC%87tmasi)

## Kaynakça

* https://tr.wikipedia.org/wiki/Birle%C5%9Ftirmeli_s%C4%B1ralama#cite_note-1
* https://www.geeksforgeeks.org/merge-sort/
* https://bidb.itu.edu.tr/seyir-defteri/blog/2013/09/08/merge-sort-(bile%C5%9Ftirme-s%C4%B1ralamas%C4%B1)-algoritmas%C4%B1
* https://www.programiz.com/dsa/merge-sort


[İçindekiler Bölüme Gitmek için Tıkla](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#inserti%CC%87on-short-eklemeli-s%C4%B1ralama-algori%CC%87tmasi)
