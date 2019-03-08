#pigeonhole
# {1,2,3,...,24}  icerisinde toplamlari 25 olan 13 ikili sayi secildiginde
#secilen sayilardan 2 tanesinin ayni olacagini ispatlayiniz.
hole=0
pigeon=13

for i in range (1,25):
    for j in range (1,25):
        if j>i:
            break
        elif i+j==25:
            hole = hole+1

if pigeon>hole: 
    print ("pigeon=",pigeon, "hole=",hole,"\n'pigeon>hole '  two of the pairs selected according to the result are the same.")

