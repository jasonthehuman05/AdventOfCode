# Advent of Code - 5th Dec

import math


inputFile = []
rules = []
updates = []

with open("input.txt") as f:
    inputFile = f.read()
    inputFile = inputFile.split("\n")
    for i in range(0, len(inputFile)):
        if "|" in inputFile[i]:
            rules.append(inputFile[i])
        elif "," in inputFile[i]:
            updates.append(inputFile[i])

# Convert rules into a list<list<int>>
for i in range(0, len(rules)):
    rules[i] = [int(num) for num in rules[i].split("|")]

# convert updates into a list<list<int>>
for i in range(0, len(updates)):
    updates[i] = [int(num) for num in updates[i].split(',')]


totalMiddlesNoSort = 0
totalMiddlesWithSort = 0

#Iterate through each update
for update in updates:
    print(update)
    validRules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            validRules.append(rule)

    # keep iterating over the list until we can make a pass of all the rules without any changes
    iterations = 0
    cleanPass = False
    while not cleanPass:
        cleanPass = True
        for rule in validRules:
            ruleLeft = update.index(rule[0])
            ruleRight = update.index(rule[1])
            if ruleRight < ruleLeft:
                vL = update[ruleLeft]
                vR = update[ruleRight]

                update[ruleLeft] = vR
                update[ruleRight] = vL

                cleanPass = False
        iterations += 1
    

    
    # get middle value
    length = len(update)
    midpoint = math.floor(length / 2)
    midValue = update[midpoint]
    
    if iterations == 1:
        totalMiddlesNoSort += midValue
    else:
        totalMiddlesWithSort += midValue

print(f"Unsorted - {totalMiddlesNoSort}")
print(f"Sorted   - {totalMiddlesWithSort}")
print(len(updates))