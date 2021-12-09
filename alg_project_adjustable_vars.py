#  =====================================================
#   Final Project Algorithm Python Variable Version 
#   2703
#   Collin Graham
#  =====================================================
#   Rate-Monotonic Scheduling Checker
#  =====================================================
#   Potential Outputs:
#       Rejected: Utilization > 100%.
#       Rejected: Failed to meet one or more deadlines.
#       Accepted: Utilization < Guarantee Level.
#       Accepted: No deadlines missed.
#  =====================================================
from math import gcd

# Adjustable. It should be noted that execTms[x] and period[x] refer to the execution time and period of Task x. 
periods = [10,15,250,170,45,37,130]
execTms = [5,5,1,1,2,1,1]

taskNum = len(periods)
a = taskNum + 1

print("\n\n\n\n\n==========================")
print(" Number of Tasks: ", taskNum)

# Calculate Utilization
utilization = 0
for x in range(len(periods)):
    utilization += execTms[x] / periods[x] 
print(" Utilization:      %.4f" % utilization)

# Case: Over Utilized
if utilization > 1: 
    utilization *= 100
    print("\n[Rejected]: Utilization > 100% (", "%3.1f" % utilization, "%)", sep='')
    print("============================")
    quit()

# Calculate Guarantee Level
g = taskNum * (2**(1/taskNum) - 1)
print(" Guarantee Level:  %.4f" % g)

# Case: Under Utilized
if utilization < g: 
    utilization *= 100
    print("\n[Accepted]: Utilization < Guarantee Level (", "%3.1f" % utilization, "%)", sep='')
    print("============================")
    quit()

# Case: Only one input (accept b/c it's garunteed < 100% util if the code has run this far)
if len(periods) == 1:
    print("\n[Accepted]: No deadlines missed.")
    print("============================")
    quit()

## Checker Alg

# Find LCM of Periods (This will be the next Critical Moment)
lcm = 1 # also equivalent to next critical moment / max cpuSched array length
for x in periods:
    lcm = lcm * x // gcd(lcm, x)

# Sort Lists
zipList = sorted(zip(periods, execTms))
periods.sort()
execTms = [x for _,x in zipList]

# Creating Vars for Algorithm
cpuSched = []
currTm = 0
currTaskLeftExec = 0

# Create Empty List
for x in range(lcm):
    cpuSched.append(0)

# Fail Func
def fail_deadline():
    print("\n[Rejected]: Failed to meet one or more deadlines.")
    print("==========================")
    quit()

# Success Func
def succeed():
    print("\n[Accepted]: No deadlines missed.")
    print("==========================")
    quit()

# Algorithm: For Each Task, go through cpuSched and schedule times. If it misses a deadline, fail it.
#       Assumptions:
#               currTm is initialized to 0
#               currTaskLeftExec is initialized to 0
#               periods and execTms are sorted lists (sorted from least period to greatest) of the period and execution times of each task 
#                   (periods[x] is the period for task x and execTms[x] is the execution time for task x).
#               lcm is the least common multiple of all of the periods
#               cpuSched is a list with range of lcm with every value initialized to 0.
#       
#       Output:
#               fail_deadline(); is called if Rate-Monotonic Scheduling will work for the given task set.
#               succeed();       is called if Rate-Monotonic Scheduling will not work for the given task set.
# 
#       Complexity:
#               O(X*Y) where X is the length of the periods list and Y is the lcm of the periods.
#
for x in range(len(periods)):
    for y in range(lcm): # for each task, go thru and schedule
        # Case: New Period
        if currTm % periods[x] == 0: # if we are on a new period
            if currTaskLeftExec != 0: # if we still had work to do
                fail_deadline()
            # if we didn't have work to do reset the counters
            currTaskLeftExec = execTms[x]

        if currTaskLeftExec > 0: # if we still have work to do
            if cpuSched[currTm] == 1: # if the timeslot is already taken
                currTm += 1
            elif cpuSched[currTm] == 0: # if the timeslot is empty
                cpuSched[currTm] = 1 # fill the timeslot
                currTaskLeftExec -= 1 # we have done one cycle for this period for this task
                currTm += 1
        elif currTaskLeftExec == 0: # if we do not have work to do
            currTm += 1
    currTm = 0

succeed()