lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "ciastko czekoladowe", "foccacia", "rogal"],
    "warzywniak": ["marchew", "seler", "rukola", "papryka", "sałata"]
}

new_list = dict()
for sklep, produkt in lista_zakupow.items():
    new_list[sklep.capitalize()] = list()
    for i in produkt:
        new_list[sklep.capitalize()].append(i.title())

x = 0
for sklep, produkt in new_list.items():
    print(f"Odiwedzam sklep {sklep} i kupuję tam {produkt}")
    x = x + len(produkt)

y = len(new_list)

print(f"Odwiedziłem {y} sklepy/ów i kupiłem w sumie {x} produktów")

print("Specjalne pozdrowienia dla Mentora :)")
print("Podaj jakąś liczbę")
x = int(input())
print(f"Mówisz, {x} ... ja mówię {x+1}, wygrałem :D ...")