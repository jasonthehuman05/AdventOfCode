# Advent of Code - 7th Dec

print(" ") # no clue why but VScode was having an issue with the terminal. This is literally just to fix that

equations = []

# Load the file and parse each line
with open("input.txt") as file:
    for line in file.readlines():
        # Separate the target value from the operands
        parts = line.strip("\n").split(": ")
        equation = []
        equation.append(parts[0]) #Get the target value and store it
        
        # Split up the operands
        operands = parts[1].split(" ")
        equation.append(operands)
        
        equations.append(equation)
        
def PartOne():
    # Iterate over each equation, checking if it has a valid option
    totalValid = 0
    for eq in equations:
        print(eq)
        target = eq[0]
        totalOperatorPositions = len(eq[1]) - 1
        for i in range(0, 2 ** totalOperatorPositions): # Iterate through each of the possible sum options
            thisSumTotal = int(eq[1][0])
            binaryNum = (bin(i)[2:]).zfill(totalOperatorPositions)
            sumString = ""
            for j in range(0, totalOperatorPositions):
                bit = binaryNum[j]
                if bit == "0": # add
                    thisSumTotal = thisSumTotal + int(eq[1][j+1])
                else: # add
                    thisSumTotal = thisSumTotal * int(eq[1][j+1])
                    
            if thisSumTotal == int(target):
                #Target found! add to total and quit loop
                totalValid += thisSumTotal
                break
        
#Option Generator Tester
def base10_to_base3(num, length):
  """Converts a base-10 number to a base-3 number.

  Args:
    num: The base-10 number to convert.

  Returns:
    The equivalent base-3 number as a string.
  """

  if num == 0:
    return '0'.zfill(length)

  base3_digits = []
  while num > 0:
    remainder = num % 3
    base3_digits.append(str(remainder))
    num //= 3

  return (''.join(reversed(base3_digits))).zfill(length)

def PartTwo():
    # Iterate over each equation, checking if it has a valid option
    numOfEqs = len(equations)
    curPos = 0
    totalValid = 0
    for eq in equations:
        curPos+=1
        print(f"{curPos} / {numOfEqs}")
        target = eq[0]
        totalOperatorPositions = len(eq[1]) - 1
        for i in range(0, 3 ** totalOperatorPositions): # Iterate through each of the possible sum options
            thisSumTotal = int(eq[1][0])
            trinaryNum = base10_to_base3(i, totalOperatorPositions)
            sumString = ""
            for j in range(0, totalOperatorPositions):
                bit = trinaryNum[j]
                if bit == "0": # add
                    thisSumTotal = thisSumTotal + int(eq[1][j+1])
                elif bit == "1": # multiply
                    thisSumTotal = thisSumTotal * int(eq[1][j+1])
                else: # do the weird concat thing
                    thisSumTotal = int(str(thisSumTotal) + eq[1][j+1]) #Lord have mercy
                    
            if thisSumTotal == int(target):
                #Target found! add to total and quit loop
                totalValid += thisSumTotal
                break
            
    print(totalValid)
    
PartTwo()