# # 13-amaliyot

# python_words = {
#     "integer": "Butun son",
#     "float": "O'nlik son",
#     "boolean": "Mantiqiy qiymat",
#     "for": "Biror amalni qayta-qayta bajarish tsikli",
#     "if": "Shartlarni tekshirish operatori",
# }

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")

# davlatlar = {
#     "o'zbekiston": "toshkent",
#     "aqsh": "washington d.c.",
#     "rossiya": "moskva",
#     "tojikiston": "dushanbe",
#     "qirg'iziston": "bishkek",
#     "qozog'iston": "nursulton",
#     "malayziya": "kuala-lumpur",
#     "singapur": "sungapur",
#     "italiya": "rim",
# }
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print("\nDavlatlarning poytaxtlari")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.)

# # Restoran menusi

# # # # dict_["ism"]="Vali"
# # print(dict_)

# menyu={
#     "osh":25000,
#     "shashlik":500000,
#     "non":10000,
#     "salat":10000,
#     "lagmon":20000,
#     "choy":3000,
#     # "kabob":180000,
#     "somsa":8000
# # }
# while True:
#     taom=input("qaysi taomni yemoqchisiz?")
#     if taom == "stop":
#     # taom in menyu:
#         print ('osh bolsin')
#         break
#     # print(menyu.get(taom,f"bizda hj{taom} yuq"))

# # my_list =['Ali','Vali','Ali','vali','vali','Oysha']
# # my_dict={

# }
# for ism in my_list:
#     my_dict[ism] = my_list.count(ism.lower())
#     print (my_dict) 

# # 14-amaliyot

# ranglar = {"qizil", "oq", "yashil"}
# ranglar.add("sariq")
# ranglar.update(["ko'k", "qora", "pushti"])

# # Umumiy elementlar
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set3 = set1 & set2
# print(set3)

# # To'plamlar orasida farq
# print(set1.difference(set2))
# print(set2.difference(set1))

# # Simmetrik farq
# print(set1.symmetric_difference(set2))""
# # To'plamga element qo'shish
# mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
# mevalar.add("banan")
# print(mevalar)
# mevalar.update(["anor", "qovun"])
# print(mevalar)

# # Element o'chirish
# mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
# mevalar.discard("anjir")
# print(mevalar)
# mevalar.remove("banan")
# print(mevalar)

# sonlar = {1, 2, 3, 4, 5, 6}
# sonlar.discard(7)
# print(sonlar)
# sonlar.remove(7)
# print(sonlar)

# sonlar = {1, 2, 3, 4, 5, 6}
# son = sonlar.pop()
# print(son)
# print(sonlar)To'plamlar ustida amallar

# # Jamlanma
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = A | B
# print(C)
# D = A.union(B)
# print(D)

# # Kesishma
# print(A & B)
# print(A.intersection(B))

# # Farq
# print(A - B)
# print(B.difference(A))

# # Simmetrik farq
# print(A ^ B)
# print(A.symmetric_difference(B))









