
mahsulot_soni = int(input("Nechta mahsulot oldiz? "))
mahsulotlar = []
for i in range(1, mahsulot_soni + 1):
    mahsulotlar.append(input(f"{i} Mahsulot nomi: "))

summa = 1
for i in mahsulotlar:
    kg = int(input(f"Necha kilo {i} oldingiz? "))
    s = int(input("Kilosi nechpul: "))
    summa += kg * s

print(f"Sizning bozorlikingiz {summa} so'm bo'ldi")
