# Obtener los inputs del txt
fichero = open("Day-2_input.txt", "r")
inputString = fichero.readline() + ","

start = 0
end = 0

wrongIDSum = 0

iteracionesTotales = 0

for i in range(inputString.count(",")):
    iteracionesTotales = iteracionesTotales + 1
    # Encontrar los intervalos
    if i == 0:
        end = inputString.find(",")
    else:
        start = end + 1
        end = inputString.find(",",start)
    intervalo = inputString[start:end]
    
    # Sacar el rango del intervalo
    primerNumero = int(intervalo[:intervalo.find("-")])
    segundoNumero = int(intervalo[intervalo.find("-")+1:])

    # Skipear rangos de longitud impar e igual, porque podria haber alguno de 1-111, y en ese caso si existirían posiblidades.
    if len(str(primerNumero)) == len(str(segundoNumero)) and not len(str(primerNumero)) % 2 == 0 and not len(str(segundoNumero)) % 2 == 0:
        continue

    # Recorremos el rango
    for j in range(primerNumero,segundoNumero+1):
        iteracionesTotales = iteracionesTotales + 1
        actualNumber = str(j)
        # Si la longitud del numero es impar, next
        if not len(actualNumber) % 2 == 0:
            continue
        
        # Fragmentamos el numero por la mitad
        primeraParte = actualNumber[:len(actualNumber) // 2 ]
        segundaParte = actualNumber[(len(actualNumber) // 2 ):]

        # Si son iguales bingo
        if primeraParte == segundaParte:
            wrongIDSum = wrongIDSum + j

print("La suma de todas las IDs erroneas es:",wrongIDSum)
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces")