#Q2
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
#Q3
aanbieding = prijzen["vanille"] * 0.8
#Q4
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
#Q5
reclame_tekst2 = reclame_tekst[:62]
#Q6
reclame_tekst3 = reclame_tekst2.upper()
#Q7
reclame_tekst4 = reclame_tekst3.split(" ")
#Q8, Q9, Q10
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el)
    else:
        print(el.lower())

