# 09-dars: for loops
# # # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
# # # va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# # ismlar = ["Olim", "Zebo", "Nazokatxon", "Bonu", "Shaxriyor"]
# # for ism in ismlar:
# #     print(f"Assalom alaykum, {ism}. Xush kelibsiz!")

# # # Yuqirdagi sikl tugaganidan so'ng,ekranga "Kod n marta takrorlandi" degan xabar chiqaring
# # # (n o'rniga kod necha marta takrorlanganini yozing)
# # print(f"Kod {len(ismlar)} marta takrorlandi")

# # # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# # # Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# # sonlar = list(range(11, 100, 2))
# # for son in sonlar:
# #     print(son ** 3)

# # kinolar = []
# # print("5 ta sevimli kinoingiz qaysilar?")
# # for k in range(5):
# #     kinolar.append(input(f"{k+1}-kino:"))
# # print(kinolar)
# # n_people = int(input("Bugun necha kishi bn suhbat qildingiz?"))
# # ismlar = []
# # for n in range(n_people):
# #     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# # print(ismlar)


# 10-amaliyot
# avtolar = ['Gentra','Tesla','Ferrari','Malibu','Tracker']
# for avto in avtolar: # avtolar ichidagi har bir avto uchun .
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ..
#         print(avto.upper()) # avto nomini hamma harflarini katta bn
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bn

#  ism = input('Ismingiz nima?\n') # Foydalanuvchi ismini so'raymiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
#     print(f"Uzr, {ism.title()} biz Alini kutayapmiz.")
# else:
#     print("Salom, Ali")

# javob = float(input("12x6 nechiga teng?"))
# if javob!=72:
#     print("Javob xato!")

# yosh = int(input("Yoshingiz nechida?"))
# if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')

# login = input("Yangi login tanlang:")
# if len(login)<=5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")

# yil = int(input("Tug'ilgan yilingizni k:"))
# if 2025-yil<18: # foydalanuvchi yoshini hisoblemiza
    # print (f"Yoshing {2025-yil}da ekan")
    # print('Kirish mumkinmas')
# else:
    # print('Xush kelibsan!')

# cars=['Tracker','Malibu 2','gm','Cobalt',"Ravon"]
# for car in cars:
    # if car == 'gm':
        # print(car.upper())
# else:
    # print(car.title())

# yosh=int(input('Yoshing nechida?'))
# if yosh>65:
    # print('San Covidga chalingansan')
# else:
    # print("Sog'lom ekansan")













