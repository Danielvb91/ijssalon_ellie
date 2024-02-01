from algemene_functies import mijn_functie_2
#Q5
def aanbieding_1(smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-prijs*korting} euro."

#Q6 & Q7
def inkomsten_totaal(inkomsten,btw=0):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

#Q8
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst),min(mijn_lijst)]

#Q9 & Q10
def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst)/len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

#Q11
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

#Q12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
