lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "ciastko czekoladowe"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

x=0
for sklep, produkt in lista_zakupow.items():
    print(f"Odiwedzam sklep {sklep} i kupuję tam {produkt}")
    x = x + len(produkt)

print(f"W sumie kupuję {x} produktów")