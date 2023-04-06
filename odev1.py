baslik = "HABERİNİZ OLSUN"
vade = 12 
faiz0rani = 1.47 
print(baslik)
print(type(baslik)) 
print(type(vade))
print(type(faiz0rani)) 
mesaj = "Hoşgeldin"
musteriAdi = "SERCAN ULAŞ"
musteriSoyadi = "AKÇAY"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!" 
print(sonucMesaj) 

sayi1 = 10 
sayi2 = 20 
print(sayi1 + sayi2)    
print(sonucMesaj)


krediler = ["hızlı kredi","Maaşını Halkbanktan alanlar","mutlu emekli ihytiyaç kredisi"]

for kredi in krediler:
    print("<option>" + kredi + "<option>" ) 

for   i in range(3,10) :
    print(i) 

for i in range(0,11,2) :
    print(i)


krediler = ["hızlı kredi","Maaşını Halkbanktan alanlar","mutlu emekli ihytiyaç kredisi"]
print(krediler) 
print(krediler[0])
print(krediler[1])
print(krediler[2]) 


print(len(krediler))

krediler[0] = "çabuk kredi"
print(krediler)



dolarDun = 7.65 
dolarBugun = 7.65

if dolarDun>dolarBugun:
    print("Azalış Oku") 
    print("Bitti")     
elif dolarDun<dolarBugun:
    print("Artış oku")


else:
    print("Eşittir Oku")      
    print("bitti")  




def kredilerilistele():
    krediler = ["hızlı kredi","Maaşını Halkbanktan alanlar","mutlu emekli ihytiyaç kredisi"]
    for kredi in krediler:
        print("<option>" + kredi + "<option>" ) 

kredilerilistele()
kredilerilistele()
kredilerilistele()
kredilerilistele()

       
        
        


        


    





    

        

        