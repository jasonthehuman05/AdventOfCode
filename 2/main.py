with open("input.txt", "r") as file:
    reportList = file.read().splitlines()


def PartOneFunct():
    SafeReports = 0
    for report in reportList:
        report = list(map(int, report.split())) # Get each row as a list of ints

        ascending = True if report[1] - report[0] > 0 else False # Is it ascending
        for i in range(0, len(report)-1): # iterate through each value in the report, comparing it to the next
            diff = report[i+1] - report[i] # Calc difference
            
            # if it is not in the acceptable change range of 1-3, or if it is not following the expected change pattern (increase / decrease) skip over
            if not 1 <= abs(diff) <= 3:
                break   # move to next report (continue outer loop)
            if (ascending and diff < 0) or (not ascending and diff > 0):
                break
            
            # If we made it to the end, add one to the safe reports counter
            if i == len(report)-2:
                SafeReports += 1

    print("Part 1:", SafeReports)


# THERE'S A PART TWO???
def PartTwoFunct(): 

    def is_safe(report): # same as above
        ascending = True if report[1] - report[0] > 0 else False # Is it ascending
        for i in range(0, len(report)-1): # iterate through each value in the report, comparing it to the next
            diff = report[i+1] - report[i] # Calc difference
            
            # if it is not in the acceptable change range of 1-3, or if it is not following the expected change pattern (increase / decrease) skip over
            if not 1 <= abs(diff) <= 3:
                return False   # move to next report (continue outer loop)
            if (ascending and diff < 0) or (not ascending and diff > 0):
                return False
            
            # If we made it to the end, add one to the safe reports counter
            if i == len(report)-2:
                return True


    SafeReports = 0
    for report in reportList:
        report = list(map(int, report.split())) # Map as ints in a list
        
        if is_safe(report):
            SafeReports += 1
            continue
                
        # apply "problem dampener" - iterate over each position and see if its valid after removing any one value
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:] #Remove the problem child
            if is_safe(modified_report):
                SafeReports += 1
                break

    print("Part 2:", SafeReports)

PartOneFunct()
PartTwoFunct()