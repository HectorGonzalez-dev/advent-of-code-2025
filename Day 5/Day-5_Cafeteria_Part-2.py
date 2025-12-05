rangesInputs = []

# Obtener los inputs del txt
fichero = open("Day-5_input.txt", "r")

for line in fichero:
    if line.replace("\n","") == "":
        break
    primerNumero = int(line.replace("\n","")[:line.find("-")])
    ultimoNumero = int(line.replace("\n","")[line.find("-")+1:])
    rangesInputs.append([primerNumero,ultimoNumero])

freshIngredients = 0
iteracionesTotales = 0

# Ordenar los inputs de menor a mayor por el ultimo numero del rango
for pasada in range(len(rangesInputs)-1):
    iteracionesTotales = iteracionesTotales + 1
    for i in range(0, len(rangesInputs)-1-pasada):
        iteracionesTotales = iteracionesTotales + 1
        if rangesInputs[i][1] > rangesInputs[i+1][1]:
            aux = rangesInputs[i+1]
            rangesInputs[i+1] = rangesInputs[i]
            rangesInputs[i] = aux

# Unificamos los rangos superpuestos
for i in range(len(rangesInputs)-1,-1,-1):
    iteracionesTotales = iteracionesTotales + 1
    if not i == 0:
        if rangesInputs[i-1][1] >= rangesInputs[i][0] and rangesInputs[i-1][0] >= rangesInputs[i][0]:
            rangesInputs[i-1] = rangesInputs[i]
            rangesInputs.remove(rangesInputs[i])
        elif rangesInputs[i-1][1] >= rangesInputs[i][0]:
            rangesInputs[i-1][1] = rangesInputs[i][1]
            rangesInputs.remove(rangesInputs[i])

# Vemos las IDs totales de los rangos resultantes
for rango in rangesInputs:
    iteracionesTotales = iteracionesTotales + 1
    freshIngredients = freshIngredients + ((rango[1]-rango[0])+1)

print("Hay un total de",freshIngredients,"IDs de ingredientes frescos")
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces") # 17.296