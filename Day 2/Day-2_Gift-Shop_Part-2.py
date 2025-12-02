# Obtener los inputs del txt
fichero = open("Day-2_input.txt", "r")
inputString = fichero.readline() + ","

start = 0
end = 0

wrongIDSum = 0

for i in range(inputString.count(",")):
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

    # Recorremos el rango
    longitudActual = 0
    divisores = []
    for j in range(primerNumero,segundoNumero+1):
        actualNumber = str(j)

        # Obtener los divisores de la longitud actual, si es la misma que la anterior no hace falta recalcularlos
        if not len(actualNumber) == longitudActual:
            longitudActual = len(actualNumber)
            divisores = []
            for k in range(1, longitudActual + 1):
                if not longitudActual == k: # Exceptuandose a si mismo
                    if longitudActual % k == 0:
                        divisores.append(k)

        for divisor in divisores:
            for k in range(j // divisor):
                print()

print("La suma de todas las IDs erroneas es:",wrongIDSum)