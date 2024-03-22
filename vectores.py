
lista_vacia = []

lista_mas_cinco = [1, 2, 3, 4, 5, 6]

longitud_lista_vacia = len(lista_vacia)
longitud_lista_mas_cinco = len(lista_mas_cinco)

primer_elemento = lista_mas_cinco[0]
elemento_central = lista_mas_cinco[len(lista_mas_cinco)//2]
ultimo_elemento = lista_mas_cinco[-1]

Datos_personales = []
Datos_personales.append("Carlos")
Datos_personales.append(20)
Datos_personales.append(2.05)
Datos_personales.append("Soltero")
Datos_personales.append("urb. villa del sol")

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

it_companies.insert(1, "carloscompany")

empresa_existe = "Microsoft" in it_companies

it_companies.sort()

it_companies.reverse()

it_companies.pop(0)

del it_companies[:]

print("Lista vacía:", lista_vacia)
print("Lista con más de 5 elementos:", lista_mas_cinco)
print("Longitud de la lista vacía:", longitud_lista_vacia)
print("Longitud de la lista con más de 5 elementos:", longitud_lista_mas_cinco)
print("Primer elemento de la lista:", primer_elemento)
print("Elemento central de la lista:", elemento_central)
print("Último elemento de la lista:", ultimo_elemento)
print("Datos personales:", Datos_personales)
print("Lista de empresas de IT:", it_companies)
print("¿Microsoft existe en la lista de empresas de IT?", empresa_existe)
