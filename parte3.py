import random

def disease_problem(n):
    ill_positives = 0
    total_positives = 0


    for i in range (n):
        is_ill = random.random() < 0.0001
        
        if is_ill:
            is_positive = random.random() > 0.01
        else:
            is_positive = random.random() < 0.02

        if is_positive:
            total_positives += 1
            if is_ill:
                ill_positives += 1
    
    if total_positives == 0:
        return 0
    else: 
        return "probability in " + str(n) + " people: " + str(ill_positives) + "/" + str(total_positives) + " = " + str(ill_positives/total_positives)
    

resultado_simulacion = disease_problem(1000000000)
print(resultado_simulacion)
