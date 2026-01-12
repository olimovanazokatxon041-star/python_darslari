# # 15-amaliyot

# buxoriy = {
#     "ism": "Abu Abdulloh Muhammad ibn Ismoil",
#     "tyil": 810,
#     "vyil": 870,
#     "tjoy": "Buxoro",
# }
# qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

# vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

# navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

# shaxslar = ['Buxoriy, Qodiriy, Vohidov, Navoiy']
# for shaxs in shaxslar:
#     ism = "Buxoriy"
#     t_yil = 1820
#     v_yil = 1900
#     t_joy = "Buxoro"
#     print(
#         f"{ism} {t_yil}-yilda {t_joy}da tavallud topgan. " 
#         f"{v_yil-t_yil} yil umr ko'rgan."
#     )
# IbnSino = {
#     "ism": "IbnSino",
#     "t_yil": 810,
#     "v_yil": 870,
#     "t_joy": "afshona",
#     "asarlar": [
#         "Al-jome as-sahih",
#         "Al-adab al-mufrad",
#         "At-tarix al-kabir",
#         "At-tarix as-sagir"
#     ]
# }
# Qodiriy = {
#     "ism": "Abdulla Qodiriy",
#     "t_yil": 1894,
#     "v_yil": 1938,
#     "t_joy": "Toshkent",
#     "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
# }
# print()
# Vohidov = {
#     "ism": "Erkin Vohidov",
#     "t_yil": 1936,
#     "v_yil": 2016,
#     "t_joy": "Farg'ona",
#     "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
# }
# Navoiy = {
#     "ism": "Alisher Navoiy",
#     "t_yil": 1441,
#     "v_yil": 1501,
#     "t_joy": "Xirot",
#     "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
# }


# # for ism, kinolar in kinolar.items():
# #     print(f"\n{ism.title()}ning sevimli kinolari:")
# #     for kino in kinolar:
# #         print(kino)

# # davlatlar = {
# #     "o'zbekiston": {
# #         "poytaxt": "toshkent",
# #         "maydon": 448978,
# #         "aholi": 33_000_000,
# #         "pul birligi": "so'm",
# #     },
# #     "rossiya": {
# #         "poytaxt": "moskva",
# #         "maydon": 17_098_246,
# #         "aholi": 144_000_000,
# #         "pul birligi": "rubl",
# #     },
# #     "aqsh": {
# #         "poytaxt": "vashington",
# #         "maydon": 9_631_418,
# #         "aholi": 327_000_000,
# #         "pul birligi": "dollar",
# #     },
# #     "malayziya": {
# #         "poytaxt": "kuala-lumpur",
# #         "maydon": 329750,
# #         "aholi": 25_000_000,
# #         "pul birligi": "rinngit",
# #     },
# # }
# # for davlat, info in davlatlar.items():
# #     if davlat.lower() == "aqsh":
# #         davlat = davlat.upper()
# #     else:
# #         davlat = davlat.capitalize()
# #     print(
# #         f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
# #         f"\nHududi: {info['maydon']} kv.km"
# #         f"\nAholisi: {info['aholi']}"
# #         f"\nPul birligi: {info['pul birligi']}"
# #     )
# #     davlatlar = {
# #     "o'zbekiston": {
# #         "poytaxt": "toshkent",
# #         "maydon": 448978,
# #         "aholi": 33_000_000,
# #         "pul birligi": "so'm",
# #     },
# #     "rossiya": {
# #         "poytaxt": "moskva",
# #         "maydon": 17_098_246,
# #         "aholi": 144_000_000,
# #         "pul birligi": "rubl",
# #     },
# #     "aqsh": {
# #         "poytaxt": "vashington",
# #         "maydon": 9_631_418,
# #         "aholi": 327_000_000,
# #         "pul birligi": "dollar",
# #     },
# #     "malayziya": {
# #         "poytaxt": "kuala-lumpur",
# #         "maydon": 329750,
# #         "aholi": 25_000_000,
# #         "pul birligi": "rinngit",
# #     },
# # }
# # davlat = input("Davlat nomini kiriting: ").lower()
# # if davlat in davlatlar:
# #     info = davlatlar[davlat]
# #     print (
# #         f"\n{davlat.capitalize()})
# #     )

# # 16-Amaliyot

# # savol = "Sevgan kitobingizni kiriting"
# # savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# # while True:
# #     kitob = input(savol)
# #     if kitob == "exit":
# #         break
# # print("Rahmat!")

# # savol = "Yoshingizni kiriting: "

# # while True:
# #     qiymat = input(savol)
# #     if qiymat == "exit" or qiymat == "quit":
# #         break
# #     yosh = int(qiymat)

# #     if yosh < 7:
# #         narh = 2000
# #     elif 7 <= yosh < 18:
# #         narh = 3000
# #     elif 18 <= yosh < 65:
# #         narh = 10000
# #     else:
# #         narh = 0

# #     if narh == 0:
# #         print("Sizga chipta bepul")
# #     else:
# #         print(f"Chipta {narh} so'm")
# # # Muzeyga chipta narhi foydalanuvchining
# # # yoshiga bog'liq:
# # # 7 dan yoshlarga - 2000 so'm,
# # # 7-18 gacha 3000 so'm,
# # # 18-65 gacha 10000 so'm,
# # # 65 dan kattalarga bepul.
# # # Shunday while tsikl yozingki,
# # # dastur foydalanuvchi yoshini so'rasin
# # # va chipta narhini chiqarsin.
# # # Foydalanuvchi exit yoki quit deb yozganda
# # # dastur to'xtasin (ikkita shartni ham tekshiring).

# # # ildizini qaytaruvchi dastur.\n"
# # savol += "Musbat son kiriting "
# # savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# # while True:
# #     qiymat = input(savol)
# #     if qiymat == "exit":
# #         break
# #     elif float(qiymat) < 0:
# #         continue  # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
# #     else:
# #         ildiz = float(qiymat) ** (0.5)
# #         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# # # 16-amaliyot

# # savat = []
# # while True:
# #     mahsulot = input("Savatga mahsulot qo'shing:")
# #     savat.append(mahsulot)
# #     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
# #     if javob != "ha":
# #         break
# # print("Dastur tugadi!")

# # mahsulotlar = {}
# # while True:
# #     mahsulot = input("Mahsulot nomini kiriting: ")
# #     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
# #     mahsulotlar[mahsulot] = narh
# #     javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
# #     if javob != "ha":
# #         break
# # print("Mahsulotlar qo'shildi")buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
# # mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

# # while buyurtmalar:
# #     buyurtma = buyurtmalar.pop()
# #     if buyurtma in mahsulotlar.keys():
# #         narh = mahsulotlar[buyurtma]
# #         print(f"{buyurtma.title()} - {narh} so'm")
# #     else:
# #         print(f"Bizda {buyurtma} yo'q")










