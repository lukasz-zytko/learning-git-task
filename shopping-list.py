lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek", "ciastko czekoladowe"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

for sklep, produkt in lista_zakupow.items():
    print(f"Odiwedzam sklep {sklep} i kupuję tam {produkt}")