inputs = []

# Obtener los inputs del txt
fichero = open("Day-1_input.txt", "r")
for line in fichero:
    inputs.append(line.replace("\n",""))

dialPos = 50
dialRange = 100 # Del 0 al 99
zeroCounter = 0
iteracionesTotales = 0

for instruction in inputs:
    iteracionesTotales = iteracionesTotales + 1
    direction = instruction[:1]
    rotation = int(instruction[1:])
    zeroCounter = zeroCounter + (rotation // dialRange)
    previousDialPos = dialPos
    if rotation % dialRange != 0:
        if direction == "L":
            dialPos = (dialPos - rotation) % dialRange
            if (dialPos > previousDialPos and previousDialPos != 0) or dialPos == 0:
                zeroCounter = zeroCounter + 1
        else:
            dialPos = (dialPos + rotation) % dialRange
            if previousDialPos > dialPos or dialPos == 0:
                zeroCounter = zeroCounter + 1

print("El dial ha pasado",zeroCounter,"veces en por el 0")
print("Para obtener este resultado se han iterado",iteracionesTotales,"veces (El minimo posible en este caso)")