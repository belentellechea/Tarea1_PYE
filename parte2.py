import random 

#PARTE 2.1
def birthday(m):
    all_birthdays = []; 
    for i in range(m):
        day = random.randint(1,364)
        if day in all_birthdays: 
            return True
        all_birthdays.append(day)
    return False 

#PARTE 2.2
def calculate_probability(iterations, m): 
    victories=0
    defeats=0
    for i in range(iterations): 
        result = birthday(m)
        if result == True: 
            victories += 1 
        else: 
            defeats += 1
    print("probability in " + str(iterations) + " iterations with "+ str(m) + " people: " +str(victories) + "/" + str(iterations) + " = " + str(victories/iterations) + " and " + str(defeats) + "/" + str(iterations) + " defeats.")

calculate_probability(1000,10)
calculate_probability(10000,10)
calculate_probability(100000,10)
print(" ")
calculate_probability(1000,20)
calculate_probability(10000,20)
calculate_probability(100000,20)
print(" ")
calculate_probability(1000,30)
calculate_probability(10000,30)
calculate_probability(100000,30)
print(" ")
calculate_probability(1000,40)
calculate_probability(10000,40)
calculate_probability(100000,40)
print(" ")
calculate_probability(1000,50)
calculate_probability(10000,50)
calculate_probability(100000,50)

#---