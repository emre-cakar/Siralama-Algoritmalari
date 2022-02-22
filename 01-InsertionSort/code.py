dizi=[89,45,68,90,29,34]
boyut=len(dizi) #Dizinin boyutu öğreniliyor. 
say=0
print("\n\n%-20s"%("Düzensiz Dizi ->"), dizi,"\n","- "*50)
for i in range(1, boyut): #dizinin 2 elemanından son değere kadar döngü kuruluyor
    indis=i #Ele alınan değerin indisi tutuluyor.
    anaDeger=dizi[indis] # Ele alınan değer tutuluyor
    for j in range(i-1, -1,-1): # Dizinin ele alınan değerden bir önceki değer ile sıfırıncı indis arası döngü kuruluyor
        if ( dizi[j]>anaDeger ): # karşılaştırma yapılıyor Büyük ise aşağıdaki kod çalışacak
            dizi[j] , dizi[indis] =  dizi[indis] , dizi[j]  # dizi yer değiştirmeleri yapılıyor.
            indis-=1; say+=1 # yer değiştirme sonucu indis değeri güncelleniyor ve adım için say değeri artırılıyor
            print("%2d%-18s"%(say,". Adım"), dizi, "\t\t", anaDeger," ile ",dizi[indis+1], " yer değiştirdi.","\n","- "*50)
            #Print ile dizi ekrana belli bir formatta yazdırılıyor. 
        else:
            break