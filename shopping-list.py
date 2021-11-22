lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "ciastko czekoladowe", "foccacia", "rogal"],
    "warzywniak": ["marchew", "seler", "rukola"]
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

print(f"W sumie kupuję {x} produktów")
