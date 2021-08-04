# The Reluctant Fizz Buzzer
# This program fizz buzzez, reluctantly
# Programming began circa July 2021
# A program by Tyler Serio
# Python 3.9.5

# Import relevant modules
import time
import random

# Define methods
def fizz_but_then_also_buzz():
    count = 0
    fizz_buzzing = 1
    print("Welcome to the illustrious FizzBuzz Program...")
    print("I'm sure you'll be happy to know I'll count these numbers whenever you force me to...")
    print("Well.... let's begin...")
    print("")
    time.sleep(2)
    while fizz_buzzing == 1:
        count += 1
        time.sleep(1)
        if count >= 101:
            break
        if (count / 3).is_integer() == True and (count / 5).is_integer() == True:
            print("FizzBuzz...")
            time.sleep(random.randint(1, 3))
        elif (count / 3).is_integer() == True:
            print("Fizz...")
            time.sleep(random.randint(1, 3))
        elif (count / 5).is_integer() == True:
            print("Buzz...")
            time.sleep(random.randint(1, 3))
        else:
            print(str(count) + ".")
            time.sleep(random.randint(1, 3))
        complain = random.randint(0, 2)
        if complain == 0:
            print(complaints[random.randint(0, len(complaints) - 1)])
            time.sleep(random.randint(1, 3))
        
        #print(random.randint(0, 1))
        #access grievances

def compile_complaints():
    file = open("List_of_grievances.txt", "r")
    global complaints
    complaints = []
    for line in file:
        complaints.append(line.strip())

# Prepare for fizz buzzing
# Count down to fizz buzzing:
# 5...
# 4...
# 3...
# 2...
# 1...
# Begin fizz buzzing
compile_complaints()
fizz_but_then_also_buzz()
