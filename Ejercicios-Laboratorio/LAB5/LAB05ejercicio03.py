lista_1_al_10 = list(range(1, 11))
lista_5_al_15 = list(range(5, 16))
lista_10_al_20 = list(range(10, 21))

conjunto_1_al_10 = set(lista_1_al_10)
conjunto_5_al_15 = set(lista_5_al_15)
conjunto_10_al_20 = set(lista_10_al_20)

conjunto_comun = conjunto_1_al_10 & conjunto_5_al_15 & conjunto_10_al_20

conjunto_union = conjunto_1_al_10 | conjunto_5_al_15 | conjunto_10_al_20

conjunto_diferencia = conjunto_1_al_10 - conjunto_10_al_20

tupla_comun = (min(conjunto_comun), max(conjunto_comun))
tupla_union = (min(conjunto_union), max(conjunto_union))
tupla_diferencia = (min(conjunto_diferencia), max(conjunto_diferencia))

print("Conjunto del 1 al 10:", conjunto_1_al_10)
print("Conjunto del 5 al 15:", conjunto_5_al_15)
print("Conjunto del 10 al 20:", conjunto_10_al_20)
print("Conjunto de números presentes en las tres listas:", conjunto_comun)
print("Conjunto de números presentes en al menos una lista:", conjunto_union)
print("Conjunto de números presentes en la primera lista pero no en la última:", conjunto_diferencia)
print("Tupla de números presentes en la intersección:", tupla_comun)
print("Tupla de números presentes en la unión:", tupla_union)
print("Tupla de números presentes en la diferencia:", tupla_diferencia)
