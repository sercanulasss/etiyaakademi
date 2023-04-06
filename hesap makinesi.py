sayi1 = int(input("sayi gir: "))
sayi2 = int(input("sayi gir: ")) 
islemsec = (input("islem: ")) 

if (islemsec == "*") :
    print(sayi1 * sayi2)


elif (islemsec == "+"):
    print(sayi1 + sayi2)


elif (islemsec == "/") and (sayi2 == 0 ):
    print("hesaplanamadi") 
elif ( islemsec == "/"): 
    print(sayi1 / sayi2)


elif (islemsec == "-"):
    print(sayi1 - sayi2) 

else:
    print("gecerli deger yok") 

