class Talaba:
    """talaba nomli klass yaratamiz"""

    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}.{self.tyil}yilda tugilganman") 

talaba1= Talaba ("Nazokatxon","Olimova", 2000)
print(talaba1.ism)
print(talaba1.familiya)
talaba1.tanishtir()









