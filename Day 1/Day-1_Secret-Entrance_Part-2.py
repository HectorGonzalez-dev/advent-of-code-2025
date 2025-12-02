inputs = []

# Obtener los inputs del txt
fichero = open("Day-1_input.txt", "r")
for line in fichero:
    inputs.append(line.replace("\n",""))

dialPos = 50
dialMin = 0
dialMax = 99
zeroCounter = 0

for instruction in inputs:
    direction = instruction[:1]
    rotation = int(instruction[1:])
    if direction == "L":
        for i in range(rotation):
            if dialPos - 1 == -1:
                dialPos = dialMax
            else:
                dialPos = dialPos - 1
            if dialPos == 0:
                zeroCounter = zeroCounter + 1
    else:
        for i in range(rotation):
            if dialPos + 1 == 100:
                dialPos = dialMin
            else:
                dialPos = dialPos + 1
            if dialPos == 0:
                zeroCounter = zeroCounter + 1

print("El dial ha pasado",zeroCounter,"veces en por el 0")