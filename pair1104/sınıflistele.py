from ogrencii import Ogrenci

from sınıf import Ogretmen

ögrenciList = []
ögretmenList = []


while(1):

    grup = int(input("öğrenci için 1,ogretmen icin 2 tikla: " ))
    islem = int(input("Yapacağiniz islemi seciniz(1 = ekleme,2=listeleme):  "))
    name = input("name: ")
    major = input("major: ")

   




    def ekleme():
        if grup == 1:
            ogrenci = Ogrenci(name,major)
            ögrenciList.append(ogrenci)
        elif grup == 2 :
            ogretmen = Ogretmen(name,major)
            ögretmenList.append(ogretmen)


    def listele():
        if grup == 1:
            for i in range(len(ögrenciList)):
                print(ögrenciList[i].name , ögrenciList[i].major)
        

    ekleme()       
    listele()

    



    









