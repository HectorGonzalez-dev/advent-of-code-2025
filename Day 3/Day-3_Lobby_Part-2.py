inputs = []
# Obtener los inputs del txt
fichero = open("Day-3_input.txt", "r")
for line in fichero:
    inputs.append(line.replace("\n",""))

totalJoltage = 0

# Recorremos todas las secuencias
for sequence in inputs:
    # Reseteamos los valores con cada nueva secuencia
    numberList = ["0","0","0","0","0","0","0","0","0","0","0","0"]
    numeroFinal = ""
    digitPosition = 0
    for i in range(len(numberList)): # Buscaremos un valor para cada numero de numberList
        for j in range(digitPosition,len(sequence)-(12-(i+1))): # Start: Posicion del ultimo numero que hemos definido, End: La longitud de la secuencia - los valores restantes que quedan por definir.
            if sequence[j] > numberList[i]: # Vamos comparando para obtener el mayor numero
                numberList[i] = sequence[j]
                digitPosition = j+1 # Al obtenerlo, le sumamos 1 a la posición para que la próxima iteración empiece desde ahí.
        numeroFinal = numeroFinal + numberList[i] # Vamos concatenando los numeros
    
    # Vamos sumando los Joltages
    totalJoltage = totalJoltage + int(numeroFinal)

print("El total de Joltage que podemos obtener es:",totalJoltage)