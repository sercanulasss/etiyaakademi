def süpersayi():
    number = int(input("Bir sayi giriniz"))
    list = []
    toplam = 0 - (number)

    for i in range(1,number+1):
     if number % i == 0:
        list.append(i)
        toplam += i

    if number == toplam:
     print("MUKEMMELSAYIDIR")
    else:
     print("MUKEMMEL SAYI DEGILDIR")


süpersayi()
 









    
    





    

    

    
    
    
    
   





