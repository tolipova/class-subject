class Auto:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    def car_details(self):
        print("Avtomobil rusumi", self.name)   
        print("Avtomobil rangi", self.color) 
        print("Avtomibil narxi", self.price)
        
    def tezlik(self):
        print("tezligi 250km/h")
    def mark(self):
        print("mark")    
 

a = Auto("turck","black",2500000) 
a.car_details()
a.tezlik()


class Sinf_xona:
    def __init__(self,name,year,gender):
        self.name = name
        self.year = year
        self.gender = gender
    def sinf_malumot(self):
        print("O'quvchining ismi familiyasi", self.name)
        print("O'quvchining tug'ilgan yili", self.year)
        print("gender", self.gender)

    def age(self) :
        print("yoshi 18 da")    
    
a = Sinf_xona ("Tolipova Shahina","2005-yil","Ayol")
a.sinf_malumot()
a.age()