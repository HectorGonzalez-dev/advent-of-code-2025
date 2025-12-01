inputs = []
# Obtener los inputs del txt
with open("Day-1_input.txt", "r", encoding="utf-8") as input:
    inputs = [line.strip() for line in input]

dialPos = 50
dialRange = 100 # Del 0 al 99
zeroCounter = 0

for instruction in inputs:
    direction = instruction[:1]
    rotation = int(instruction[1:])
    if direction == "L":
        dialPos = (dialPos - rotation) % dialRange
    else:
        dialPos = (dialPos + rotation) % dialRange
    if dialPos == 0:
        zeroCounter = zeroCounter + 1

print("El dial ha apuntado",zeroCounter,"veces en el 0")