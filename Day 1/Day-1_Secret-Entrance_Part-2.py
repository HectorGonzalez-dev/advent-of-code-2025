inputs = []
# Obtener los inputs del txt
with open("Day-1_input.txt", "r", encoding="utf-8") as input:
    inputs = [line.strip() for line in input]

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

print("El dial ha pasado",zeroCounter,"veces por el 0")