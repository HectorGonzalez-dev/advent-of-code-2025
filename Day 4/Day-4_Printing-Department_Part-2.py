inputs = []
# Obtener los inputs del txt
fichero = open("Day-4_input.txt", "r")
for line in fichero:
    inputs.append(line.replace("\n",""))

eliminacionesTotales = 0
eliminacionesRonda = 0
iteracionesTotales = 0

while eliminacionesRonda > 0:
    eliminacionesRonda = 0
    for fila in range(len(inputs)):
        iteracionesTotales = iteracionesTotales + 1
        for columna in range(len(inputs[fila])):
            iteracionesTotales = iteracionesTotales + 1
            surroundingRolls = 0
            # Recorremos los numeros circundantes de nuestra posicion actual.
            for desplazamiento_fila in range(-1,2):
                iteracionesTotales = iteracionesTotales + 1
                if surroundingRolls >= 4:
                    break
                for desplazamiento_columna in range(-1,2):
                    iteracionesTotales = iteracionesTotales + 1
                    if surroundingRolls >= 4:
                        break
                    # Calculamos la posicion de los vecinos, tu posición actual + el "offset", que es con lo que recorremos los numeros circundantes.
                    fila_vecina = fila + desplazamiento_fila
                    columna_vecina = columna + desplazamiento_columna
                    # Si nuestra posición actual es la misma que la del offset pasamos.
                    if fila_vecina == fila and columna_vecina == columna:
                        continue
                    # Aseguramos que nuestra posición no esta fuera de los límites de la matriz.
                    elif 0 <= fila_vecina < (len(inputs)) and 0 <= columna_vecina < (len(inputs[fila])):
                        if inputs[fila_vecina][columna_vecina] == "@":
                            surroundingRolls = surroundingRolls + 1
            if surroundingRolls < 4 and inputs[fila][columna] == "@":
                inputs[fila] = inputs[fila][:columna] + "." + inputs[fila][columna+1:]
                eliminacionesTotales = eliminacionesTotales + 1
                eliminacionesRonda = eliminacionesRonda + 1

print("Se pueden eliminar un total de",eliminacionesTotales,"rollos de papel")
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces") # 213.718