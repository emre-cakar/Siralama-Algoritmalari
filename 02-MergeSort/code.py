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