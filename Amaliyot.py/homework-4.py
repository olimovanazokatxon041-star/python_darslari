#  7-amaliyot
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
# Ro'yxatdagi har bir do'stingizga qisqa xbar yozish
print("Salom " + ismlar[0] + "nima yangilikla?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] +' '+ "kitob o'qiyapti")

# # sonlar royxati (musbat, manfiy, butun, o'nlik).
# sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_68_00, 12.4]
# print(sonlar)
# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 37
# del sonlar[5]
# print(sonlar)

# t_shaxslar = ["Temur", "Navoiy", "Ulug'bek"]
# z_shaxslar = ["Lola", "Nazokatxon", "Bonu"]

# # (.pop()),ko'rinisda chiqaring.
# print(
#     f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# suhbat qilishni istar edim\n"
# )

# # friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append("Lola")
# friends.append("Nazo")
# friends.append("Bonu")
# friends.append("Pari")
# friends.append("Guli")
# print(friends)

# # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# friends.remove("Guli")
# friends.remove("Lola")
# print(friends)

# # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.append("Olim")
# friends.insert(0, "Zebo")
# friends.insert(2, "Jonim")
# print(friends)

# # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)


#  8-amaliyot

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing
davlatlar = ["Kanada", "Yangi Zelandiya", "Kambodja", "", "Boliviya", "Amsterdam"]
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqarish
print(len(davlatlar))

# sorted() funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqarish
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqarish
print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqarish
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqarish
davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqarish
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzish
sonlar = list(range(120, 1200))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqarish
print(sum(sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqarish
print(max(sonlar) - min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblash
print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqarish
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:550])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["osh", "somsa", "pechak", "shashlik", "sho'rva"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("pechak")
nonushta.remove("shashlik")
nonushta.remove("sho'rva")
nonushta.append("non va qaymoq")
nonushta.append("patir")

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqarish
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantirish va nonushta[0] = "qaymoq va non" deb qiymat berish.
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"













