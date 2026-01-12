# # # # 11-amaliyot
# # # son = float(input('Juft sonni k:'))
# # # if son % 2 != 0:
# # #     print('Bu son juft emas')
# # # else:
# # #   print('Thanks')

# # yosh=int(input('Yoshingizni k:'))
# # if yosh <= 4 or yosh >= 60:
# #     narx = "bepul"
# # elif yosh < 18:
# #     narx= 10000
# # else:
# #     narx=20000
# #     print(f"Chipta {narx} so'm")

x=float(input('Birinchi sonni k:'))
y=float(input('Ikkinchi sonni k:')) 
if x == y:
    print(f"{x} = {y}")
elif x < y:
    print(f"{x} < {y}")
else:
    print(f'{x} > {y}')

# mahsulotlar=[
#     'un',
#     'sovun',
#     'kartoshka',
#     'piyoz',
#     'tuxum',
#     'banan',
#     'sabzi',
#     'guruch',
#     'tuz',
#     'uzum'
# ]
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} -mahsulotni qo'shing:"))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:   
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh!")



# 12-amaliyot


# users=['Zebo','Olim','Nazo','Bonu']
# login=input('Yangi login tanlang:')
# if login in users:
    # print('Login band,yangi login tanlang!')
# else:
    # print('Xush kelibsan!')

# son= int(input('Istalgan butun son k:'))
# for n in range(2,11):
    # if not (son % n):
        # print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")

 # otam = {"ismi": "Olim", "tyil": 1978, "viloyat": "Qashqadaryo"}
# # tyil = otam["tyil"]
# # vil = otam["viloyat"]
# # print(
# #     f"Otamning ismi {'Olim'.title()}, {1978}-yilda, {'Qashqadaryo'.title()} viloyatida tug'ilgan"
# # )

 # # taomlar = {
# # #     "ali": "osh",
# # #     "vali": "shashlik",
# # #     "hasan": "lag'mon",
# # #     "husan": "mastava",
# # #     "olim": "somsa",
# # # }

# # # taom = taomlar["ali"]
# # # print(f"Alining sevimli taomi {taom}")

# print('python_izohli_lugati'['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print('python_izohli_lugati'.get(kalit, "Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = 'python_izohli_lugati'.get(kalit)
# if tarjima == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima}")







