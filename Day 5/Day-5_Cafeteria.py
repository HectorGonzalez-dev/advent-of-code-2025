rangesInputs = []
idInputs = []

# Obtener los inputs del txt
fichero = open("Day-5_input.txt", "r")

for line in fichero:
    if not line.replace("\n","").isdigit() and not line.replace("\n","") == "":
        rangesInputs.append(line.replace("\n",""))
    elif not line.replace("\n","") == "":
        idInputs.append(int(line.replace("\n","")))

freshIngredients = 0
iteracionesTotales = 0

for id in idInputs:
    iteracionesTotales = iteracionesTotales + 1
    for rango in rangesInputs:
        iteracionesTotales = iteracionesTotales + 1
        primerNumero = int(rango[:rango.find("-")])
        ultimoNumero = int(rango[rango.find("-")+1:])
        if primerNumero <= id <= ultimoNumero:
            freshIngredients = freshIngredients + 1
            break

print("Hay un total de",freshIngredients,"ingredientes frescos")
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces") # 95.313