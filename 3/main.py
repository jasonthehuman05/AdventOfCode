# Advent of Code - 3rd Dec
# According to the brief, we only want instructions that follow the exact pattern of mul(x,y) where X and Y are numerical values
# This will probably be best achieved with a regex
import re

inputText = ""

#Load the file
with open("input.txt") as file:
    inputText = file.read().replace('\n', '')

def PartOne(inputText):
    output = 0
    #Sanitize the input
    inputText = re.findall("mul\\([0-9]+,[0-9]+\\)", inputText)

    for instruction in inputText:
        #get the numbers we need
        instruction = list(map(int,instruction[4:-1].split(",")))
        
        #multiply them
        instruction = instruction[0] * instruction[1]
        #Add them to our result
        output += instruction

    print(output)

def PartTwo(inputText):
    output = 0
    #Sanitize the input
    inputText = inputText.replace("don't()", "\ndon't()")
    inputText = inputText.replace("do()", "\ndo()")

    inputText = inputText.split("\n")
    
    for line in inputText:
        if "don't()" in line:
            continue
        print(line)
        line = re.findall("mul\\([0-9]+,[0-9]+\\)", line)
        for instruction in line:
            #get the numbers we need
            instruction = list(map(int,instruction[4:-1].split(",")))
            
            #multiply them
            instruction = instruction[0] * instruction[1]
            #Add them to our result
            output += instruction
    print(output)



PartTwo(inputText)