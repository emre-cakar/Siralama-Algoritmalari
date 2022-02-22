dizi=[89,45,68,90,29,34]
def insertionSort(dizi,indis):
    if indis<len(dizi):
        for i in range(indis-1,-1,-1):
            if (dizi[i]>dizi[indis]):
                dizi[i],dizi[indis]=dizi[indis], dizi[i]
                indis-=1
            else:
                return insertionSort(dizi,indis+1)
        return insertionSort(dizi,indis+1)
    else:
        return dizi


print(insertionSort(dizi,1))