# Ce programme va impementer la méthode de rectangle, de trapèze pour passer de signal continue à un signal numérique (UE_SSS(COURS D'AUTOMATIQUE))
# nous allons implementer les differentes méthodes pour la réalisation du projet
import numpy
# fonction de convertion d'expression
def convertir_fonction(expression):
    return lambda t:eval(expression)
fonction=convertir_fonction("2*t")

# fonction calcule surface
def calcul_surface(temp_initial,temp_final):
    return fonction(temp_initial)*(temp_final-temp_initial)

#boucle pour parcourir tous les triangles
def Echantillon(temps_initial,temps_final,periode):
    stockage=0.0
    for i in range(int((temps_final-temps_initial)/periode)):
        stockage+= calcul_surface(temps_initial,temps_initial+periode)
        temps_initial+=periode  
    return stockage

print(Echantillon(0,20,2))
