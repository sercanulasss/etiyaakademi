class Ogrenci():
    def __init__(self,name,major):
        self.name = name
        self.major = major
    
    def talk(self,message):
        print(f"{self.name}: {message}")

    def davranis(self):
        print(f"{self.name}  is cok konusuyor")


