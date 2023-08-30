edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


edades.sort()
edad_minima = edades[0]
edad_maxima = edades[-1]


edades.append(edad_minima)
edades.append(edad_maxima)


longitud = len(edades)
if longitud % 2 == 1:
    edad_mediana = edades[longitud // 2]
else:
    medio1 = edades[longitud // 2 - 1]
    medio2 = edades[longitud // 2]
    edad_mediana = (medio1 + medio2) / 2


edad_promedio = sum(edades) / len(edades)


rango_edades = edad_maxima - edad_minima


diferencia_min_promedio = abs(edad_minima - edad_promedio)
diferencia_max_promedio = abs(edad_maxima - edad_promedio)

print("Lista de edades:", edades)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de edades:", rango_edades)
print("Diferencia entre mínimo y promedio:", diferencia_min_promedio)
print("Diferencia entre máximo y promedio:", diferencia_max_promedio)
