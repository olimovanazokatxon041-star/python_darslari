class Talaba:
    """Talaba nomli klass yaratamiz"""

def __init__(self,ism,familiya,tyil):
    """talabaning xususiyatlari"""
    self.ism=ism
    self.familiya=familiya
    self.tyil=tyil

def get_name(self):
    """talabani ismini q"""
    return self.ism

def get_lastname(self):
    """talabani ism-familiyasini q"""
    return f"{self.ism} {self.familiya}"

def get_age(self,yil):
    """talabani yoshini q"""
    return yil - self.tyil

def tanishtir(self):
    print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tugilgan")

talaba1 = Talaba("Sevinch", "Olimova", 2000)
print(talaba1.get_fullname())
print(talaba1.get_age(2021))



