# INSERTİON SHORT (Eklemeli Sıralama) ALGORİTMASI

## İçindekiler 
- [Insertion Sort Nedir](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#insertion-sort-nedir)
- [Algoritma Nasıl Çalışır](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#algoritma-nas%C4%B1l-%C3%A7al%C4%B1%C5%9F%C4%B1r-s%C3%B6zde-kod)
- [Örnek Çalışma](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#%C3%B6rnek-%C3%A7al%C4%B1%C5%9Fma)
- [En İyi Durum ve En Kötü Durum](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#en-i%CC%87yi-durum-ve-en-k%C3%B6t%C3%BC-durum)
- [Karmaşıklık Hesabı](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#karma%C5%9F%C4%B1kl%C4%B1k-hesab%C4%B1) 
- [Kaynakça](https://github.com/emre-cakar/Siralama-Algoritmalari/tree/main/01-InsertionSort#kaynak%C3%A7a)
---

 ## Insertion Sort Nedir?

Varolan bir diziyi (sıralı-sırasız) belli bir işlem adımları uygulayarak diziyi sıralama işlemidir. Küçük boyutlu dizilerde hızlı olsa da çok boyutlu dizilerde diğer sıralama algoritmalarına göre yavaş kalmaktadır. Bir azalt fethet algoritmasıdır. Sıralama yaparken değerleri tek tek kontrol ederek kıyaslama yapar ve sıraya koyar. 


 ## Algoritma Nasıl Çalışır (Sözde Kod)

1. İkinci indisi Al.
2. Bir önceki indisle karşılaştır. 
3. Büyükse yer değiştir değilse bir önceki indise geç
4. Dizinin başına varınca karşılaştırma indisinde bir sonraki indise geç
    * Üçüncü indisi al
    * İkinci indisle karşılaştır. 
    * Büyükse yer değiştir değilse bir önceki indisle karşılaştır
    * Dizin başına ulaşınca karşılaştırma indisinde bir sonraki indise geç

Yukarıdaki gibi işlemler devam eder. 

 ## Örnek Çalışma


* Elimizde aşağıdaki gibi bir dizi olduğunu düşünelim. 

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |

---

* Dizinin ikinci indisinden algoritma başlatılır. Önceki değerlere bakılarak büyükse yer değiştirme yapılır küçük ise  yapılmaz. 

    *   **89** değeri **45** değerinden büyük olduğu için yer değiştirme **yapılır**.

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |
    | 1. Adım   |   **45**   |   **89**   |   68   |   90   |   29   |   34   |

---

* Dizinin üçüncü indisi ele alınır. Kendinden önceki değerler ile kıyaslanır. Değerler büyükse yer değiştirilir değilse yer değiştirme yapılmaz. 
    * **89** değeri **68** değerinden büyük olduğu için yer değiştirme **yapılır.** 
    * **45** değeri **68** değerinden küçük olduğu için yer değiştirme **yapılmaz.** 

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |
    | 1. Adım   |   **45**   |   **89**   |   68   |   90   |   29   |   34   |
    | 2. Adım   |   **45**   |   **68**   |   **89**   |   90   |   29   |   34   |

---

* Dizinin dördüncü indisi ele alınır. Kendinden önceki değerler ile kıyaslanır. Değerler büyükse yer değiştirilir değilse yer değiştirme yapılmaz. 
    * **89** değeri **90** değerinden küçük olduğu için yer değiştirme **yapılmaz**
    * 89 değerinden önceki değerler sıralı olduğu için incelemeye gerek kalmaz ve bir sonraki indise geçilir.

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |
    | 1. Adım   |   **45**   |   **89**   |   68   |   90   |   29   |   34   |
    | 2. Adım   |   **45**   |   **68**   |   **89**   |   90   |   29   |   34   |
    | 3. Adım   |   **45**   |   **68**   |   **89**   |   **90**   |   29   |   34   |
---
    
    
* Dizinin beşinci indisi ele alınır. Kendinden önceki değerler ile kıyaslanır. Değerler büyükse yer değiştirilir değilse yer değiştirme yapılmaz. 
    * **90** değeri **29** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **89** değeri **29** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **68** değeri **29** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **45** değeri **29** değerinden büyük olduğu için yer değiştirme **yapılır**

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |
    | 1. Adım   |   **45**   |   **89**   |   68   |   90   |   29   |   34   |
    | 2. Adım   |   **45**   |   **68**   |   **89**   |   90   |   29   |   34   |
    | 3. Adım   |   **45**   |   **68**   |   **89**   |   **90**   |   29   |   34   |
    | 4. Adım   |   **29**   |   **45**   |   **68**   |   **89**   |   **90**   |   34   |
---

* Dizinin altıncı indisi ele alınır. Kendinden önceki değerler ile kıyaslanır. Değerler büyükse yer değiştirilir değilse yer değiştirme yapılmaz. 
    * **90** değeri **34** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **89** değeri **34** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **68** değeri **34** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **45** değeri **34** değerinden büyük olduğu için yer değiştirme **yapılır**
    * **29** değeri **34** değerinden küçük olduğu için yer değiştirme **yapılmaz**

    | Adımlar   |   ----    |   ----    |   ----    |   ----    |   ----    |   ----    |
    | :---      |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |   :----:  |
    | Ham Dizi   |   89   |   45   |   68   |   90   |   29   |   34   |
    | 1. Adım   |   **45**   |   **89**   |   68   |   90   |   29   |   34   |
    | 2. Adım   |   **45**   |   **68**   |   **89**   |   90   |   29   |   34   |
    | 3. Adım   |   **45**   |   **68**   |   **89**   |   **90**   |   29   |   34   |
    | 4. Adım   |   **29**   |   **45**   |   **68**   |   **89**   |   **90**   |   34   |
    | 4. Adım   |   **29**   |   **34**   |   **45**   |   **68**   |   **89**   |   **90**   |
    
---

* Son indis değeri de kıyaslaması bitince dizi sıralanmış olunur. 

 ```
 Sıralı Dizi :
29 34 45 68 89 90
 ``` 

![img](https://github.com/emre-cakar/Siralama-Algoritmalari/blob/main/01-InsertionSort/Example.png?raw=true)

## En İyi Durum ve En Kötü Durum 

**En iyi durum** dizinin **sıralı** olmasıdır.  Karmaşıklığı O(n-1)

**En kötü durum** ise dizinin **ters sıralı** olmasıdır. Karmaşıklığı O(n^2)

## Karmaşıklık Hesabı

Eklemeli sıralama algoritmasının zaman karmaşıklığı hesaplanırken, yapılan karşılaştırmalar ve yer değiştirmeler dikkate alınır. Eklemeli sıralama algoritması n elemanlı bir listede, ikinci eleman için en fazla 1 karşılaştırma ve 1 yer değiştirme yapar, üçüncü eleman için 2 karşılaştırma ve 2 yer değiştirme, dördüncü eleman için 3 karşılaştırma ve 3 yer değiştirme yapar. Bu şekilde son eleman için en fazla n-1 karşılaştırma ve n-1 yer değiştirme yapar. Listedeki bütün elemanlar için yapılan karşılaştırmaların ve yer değiştirmelerin toplamı : 
 
 ``` 
 n-1 + n-2 + n-3 + .... + 1
```

Yukarıda dikatli bakıldığında 1 den n-1 sayısına kaadar olan sayıların toplamını vermektedir. Matematiksel formül uyguladığımız da :

(n-1) * (n-2)/2 = (n^2 - 3n +2) / 2 

Sonuç n karedir. Bu durumda karmaşıklık: **O(n^2)**

[![](https://img.youtube.com/vi/OGzPmgsI-pQ/maxresdefault.jpg)](https://youtu.be/OGzPmgsI-pQ)


## Kaynakça

* https://tr.wikipedia.org/wiki/Eklemeli_s%C4%B1ralama
* https://www.geeksforgeeks.org/insertion-sort/