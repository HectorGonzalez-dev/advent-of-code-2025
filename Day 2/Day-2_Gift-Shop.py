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

    # Obtenemos la primera mitad del primer numero del rango
    candidateSlice = ""
    if not len(str(primerNumero)) % 2 == 0:
        candidateSlice = ("1" + "0"*len(str(primerNumero)))
    else:
        candidateSlice = str(primerNumero)[:len(str(primerNumero))]
    candidateSlice = candidateSlice[:len(candidateSlice) // 2]

    # Analizamos los posibles candidatos de cada rango en vez de recorrer todos los numeros.
    candidate = 0
    while candidate <= segundoNumero:
        iteracionesTotales = iteracionesTotales + 1
        candidate = int(candidateSlice*2)
        if candidate <= segundoNumero and candidate >= primerNumero:
            wrongIDSum = wrongIDSum + candidate
        candidateSlice = str(int(candidateSlice) + 1)

print("La suma de todas las IDs erroneas es:",wrongIDSum)
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces") # Record actual: 873