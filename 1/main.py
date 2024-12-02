# Advent of Code - 1st Dec 

leftList = []
rightList = []

# Get the sides of our list
with open("input.txt", "r") as file:
    for line in file.readlines():
        parts = line.split()
        leftList.append(int(parts[0]))
        rightList.append(int(parts[1]))

# Sort the lists
leftList.sort()
rightList.sort()

#Iterate through, calculating our values (left + right)
totalDistance = 0

for i in range(0, len(leftList)):
    totalDistance += abs(leftList[i] - rightList[i])

print(totalDistance)