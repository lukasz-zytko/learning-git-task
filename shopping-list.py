lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "ciastko czekoladowe"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

new_list = dict()
for sklep, produkt in lista_zakupow.items():
    new_list[sklep.capitalize()] = list()
    for i in produkt:
        new_list[sklep.capitalize()].append(i.title())


for sklep, produkt in new_list.items():
    print(f"Odiwedzam sklep {sklep} i kupuję tam {produkt}")