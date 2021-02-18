# Dice rolling  Library, Mercer Kenyon, Feburary 12, 2021, 1:50PM v0.1

import random 
import time

# d4 simulator 
def roll_d4(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,4)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum
    
roll_d4(5)


def roll_d6(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,6)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum


def roll_d8(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,8)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum


    def roll_d10(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,10)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum


    def roll_d12(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,12)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum


    def roll_d20(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,20)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum


    def roll_d100(num_roll): #num_roll is an ARGUMENT
    rolls = 0 
    the_sum = 0 

    while rolls < num_roll:
        result = random.randint (1,100)
        print(f"The dice gods have given you a {result}.\n")
        time.sleep(1)
        rolls += 1
        the_sum += result
    print(f"The total of the {num_roll} rolls was {the_sum}\n") #Use this line to print the sum