print("Merhaba Etiya")
text = "merhaba"

print(text)
print(text)
print(text)
text = "selam"
print(text)
print(text)

studentcount = 45
print(studentcount + 5) 
print(type(studentcount)) 
studentcountt = 25.5 
print(studentcountt + 5)

print(type(studentcountt)) 

number = 10

print(number + 5) 
print(number/2) 
print(number % 3) 
print(number == 11) 
print(number != 10) 
print( number + ((number * 2) * (number / 2 ))) 

print(number >=10 ) 
print("*******")


sayilar = [100, 200, 300, 400, 500, "merhaba"] 
print(sayilar[0])  
print(sayilar[5])

print(sayilar)
sayilar.append(600)
sayilar.append(100)
print(sayilar) 

sayilar.remove(100) 
print(sayilar) 
sayilar.extend([500,600,800,900]) 
print(sayilar) 

sayilar.clear() 
print(sayilar) 
hello = "Merhaba"
userName = "Halit" 
totaltext = f"Hoşgeldin {hello} , {userName}" 
print(totaltext) 




vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz. 

if final<40 :
    print("kaldi") 

elif ortalama <50:
    print("kaldi") 
if (vize == final*2) :
    print("kaldi")
         
else:
    print("gecti")     
         





















