inputs = []
# Obtener los inputs del txt
fichero = open("Day-3_input.txt", "r")
for line in fichero:
    inputs.append(line.replace("\n",""))

totalJoltage = 0
iteracionesTotales = 0

# Recorremos todas las secuencias
for sequence in inputs:
    # Reseteamos los numeros con cada nueva secuencia
    firstNumber = "0"
    secondNumber = "0"
    for i in range(len(sequence)): # Recorremos todos los numeros de la secuencia
        iteracionesTotales = iteracionesTotales + 1
        if firstNumber == "9" and secondNumber == "9": # Si ambos numeros son 9, ya es el maximo posible. Ahorramos iteraciones.
            break
        if not i == len(sequence) - 1: # Si no estamos en el ultimo numero, comparamos ambos numeros
            if sequence[i] > firstNumber:
                firstNumber = sequence[i]
                secondNumber = "0"
            elif sequence[i] > secondNumber:
                secondNumber = sequence[i]
        elif sequence[i] > secondNumber: # Si estamos en el ultimo numero, solo comparamos el segundo.
            secondNumber = sequence[i]
    
    # Vamos sumando los Joltages
    totalJoltage = totalJoltage + int(firstNumber + secondNumber)

print("El total de Joltage que podemos obtener es:",totalJoltage)
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces")