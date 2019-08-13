import statistics
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

# 1. Calculate the number of stops.

print("El numero de paradas totales es de:", len(stops))

# 2. Assign a variable a list whose elements are the number of passengers in each stop: 
# Each item depends on the previous item in the list + in - out.

lista_pasajeros = []
pasajeros_totales = 0

for stop in stops:
    pasajeros_totales = pasajeros_totales + stop[0] - stop[1]
    lista_pasajeros.append(pasajeros_totales)


print("LISTA DE PASAJEROS EN CADA PARADA:",lista_pasajeros)

# 3. Find the maximum occupation of the bus.

print("El numero maximo de pasajeros es:",max(lista_pasajeros))

# 4. Calculate the average occupation. And the standard deviation.

print("la media de pasajeros es:",sum(lista_pasajeros)/len(lista_pasajeros))

print("La desviacion estandar es",statistics.stdev(lista_pasajeros))

