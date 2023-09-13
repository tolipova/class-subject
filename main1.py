# class Hayvonlar:
#     def __init__(self,name,color,len,yashash_joyi):
#         self.name = name
#         self.color = color
#         self.len = len
#         self.yashash_joyi = yashash_joyi

#     def  hayvonlar_malumoti(self) :
#         print("nomi",self.name)
#         print("rangi",self.color)
#         print("Kattaligi",self.len,"sm")
#         print("doimiy yashaydi",self.yashash_joyi,"da")

# print("Yirtqich hayvonlar")
# a=Hayvonlar("Tulki","to'q sariq",45,"o'rmon")
# a.hayvonlar_malumoti()
# print()
# a=Hayvonlar("Bo'ri","qora",70,"o'rmon")
# a.hayvonlar_malumoti()
# print()
# a=Hayvonlar("Maymun","jigar rang",55,"o'rmon")
# a.hayvonlar_malumoti()
# print()

# print("Uy hayvonlari")
# a=Hayvonlar("quyon","oq",45,"uyda")
# a.hayvonlar_malumoti()
# print()
# a=Hayvonlar("qo'y","qora",90,"uyda")
# a.hayvonlar_malumoti()
# print()


# print("Qushlar")
# a=Hayvonlar("qarg'a","qora",35,"hohlagan joyida")
# a.hayvonlar_malumoti()
# print()
# a=Hayvonlar("tovuq","oq",45,"uyda")
# a.hayvonlar_malumoti()



class Hayvonlar:
    def __init__(self,name):
        self.name = name
    def yemish(self) :
        print(f"{self.yemish} yemak yeydi")


class Yirtqich(Hayvonlar):
    def __init__(self, name , ovqat_turi):
        super().__init__(name)
        self.ovqat_turi = ovqat_turi
    def ovqat_tayyorlash(self):
        print(f"{self.name}{self.ovqat_turi}tayyorlab yeydi")

class Uy_h(Hayvonlar):
    def __init__(self, name , ovqat_turi):
        super().__init__(name)
        self.ovqat_turi = ovqat_turi
    def ovqat_tayyorlash(self):
        print(f"{self.name}{self.ovqat_turi}tayyorlab yeydi")

class Dengiz_h(Hayvonlar):
    def __init__(self, name , ovqat_turi):
        super().__init__(name)
        self.ovqat_turi = ovqat_turi
    def ovqat_tayyorlash(self):
        print(f"{self.name}{self.ovqat_turi}tayyorlab yeydi")

print("Yirtqich hayvonlar")
yirtqich=Yirtqich("tulki"," gushtli ovqat ")
yirtqich.ovqat_tayyorlash()

yirtqich=Yirtqich("Maymun"," banan ")
yirtqich.ovqat_tayyorlash()
print()

print("Dangiz hayvonlari")
dengiz_hayvon=Dengiz_h("baliq"," nimadur ")
dengiz_hayvon.ovqat_tayyorlash()