# # # # # # a=int(input("birinchi sonni k:"))
# # # # # # b=int(input("ikkinchi sonni k:"))
# # # # # # c=int(input("uchinchi sonni k:")

# # # # # ismlar = ['ALi', 'Vali','Asilbek','Anora','Olim']
# # # # # ismlar.sort()
# # # # # for ism in ismlar:
# # # # #     if ism.lower().startswith('a'):
# # # # #         print(ism)
# # # # ismlar = ['ALibek', 'Valibek','Asilbek','Anora','Olimbek']
# # # # for ism in ismlar:
# # # #     if ism[-3: ].lower()=='bek':
# # # #         print(ism)

# # # # 12.19.2025
# # # dict_={
# # #     "ism":"Ali",
# # #     "yosh":45,
# # #     "familiya":"Valiyev"
# # # }
# # # print(len(dict_))
# # # print(dict_.get("ism","karta raqam mavjud emas"))
# # # dict_.update({
# # #     "username":"ali01",
# # #     "prof_pic":"https://example.com/user_1"
# # # })
# # # dict_["ism"]="Vali"
# # # # print(dict_)

# # menyu={
# #     "osh":25000,
# #     "shashlik":500000,
# #     "non":10000,
# #     "salat":10000,
# #     "lagmon":20000,
# #     "choy":3000,
# #     # "kabob":180000,
# #     "somsa":8000
# # # }
# # while True:
# #     taom=input("qaysi taomni yemoqchisiz?")
# #     if taom == "stop":
# #     # taom in menyu:
# #         print ('osh bolsin')
# #         break
# #     # print(menyu.get(taom,f"bizda hj{taom} yuq"))

# my_list =['Ali','Vali','Ali','vali','vali','Oysha']
# my_dict={

# }
# for ism in my_list:
#     my_dict[ism] = my_list.count(ism.lower())
#     print (my_dict)
    


menyu = {
    'osh': 25000,
    'shashlik': 50000,
    'non': 10000,
    'salat': 10000,
    'lagmon': 20000,
    'choy': 5000,
    'kabob': 70000
}
# 6-dars
while True:
    taom = input('Qaysi ovqatni buyurtma qilasiz?')
    if taom == 'stop':
        taom in menyu
        print ("Osh bo'lsin!")
        break
    else:
        print(menyu.get(taom,f"Bizda {taom} yo'q"))



