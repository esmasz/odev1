# odev1
#pigeonhole
güvercin yuvasi ilkesine göre; N ve k pozitif tamsayilar olsun ve N > k olmak uzere N nesne k kutuya yerlestirildiginde oyle bir kutu vardır ki o kutuda birden cok nesne bulunmak zorundadır.
Bu aciklama dogrultusunda yazilan kod  ve ilgili kodun guvercin yuvasi prensibine gore ispati verilmektedir.

#{1,2,3,...,24}  icerisinde toplamlari 25 olan 13 ikili sayi secildiginde
#secilen ikili sayilardan 2 tanesinin ayni olacagini ispatlayiniz.

                     hole=0 # yuva sayisi
                    pigeon=13 #güvercin saiyisi
                     for i in range (1,25): 
                     for j in range (1,25):
                     if j>i: #listede secilen elemanlarin tekrarinin önlenmesi
                       break
                    elif i+j==25: 
                      hole = hole+1
                if pigeon>hole: # guvercin sayisi yuva sayisindan buyuk oldugunda mutlaka bir yuvada iki guvercin bulunur prensibine gore.
                print ("pigeon=",pigeon, "hole=",hole,"\n'pigeon>hole '  two of the pairs selected according to the result are the same.")
 
 

Ornek kapsamında 1,2,..,24 arasinda listelenen sayilarin arasindan birbirini tekrarlamayan ikili gruplar olusturulmus ve iclerinden 13 adet ikili secilmesi istenmistir.

Gruplar: (1,24),(2,23),(3,22),...,(12,13) olmak uzere 12 adettir.Bu secilecek olan yuva sayisini temsil eder.

secilecek olan 13 sayi yukarida listelenen kume icerisinden olmakla birlikte elimizde bulunan guvercin sayisini temsil eder.
12 adet sayı kumesinden 13 adet secilen eleman dogrultusunda  bir elemandan iki tane secilmesinin muhakkak oldugu ispatlanmaktadir.
