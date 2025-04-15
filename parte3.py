import random

def simular_test(n):
    positivos_y_enfermos = 0
    total_positivos = 0

    for _ in range(n):
        tiene_enfermedad = random.random() < 0.0001

        if tiene_enfermedad:
            test_positivo = random.random() > 0.01  # 1% de falsos negativos
        else:
            test_positivo = random.random() < 0.02  # 2% de falsos positivos

        if test_positivo:
            total_positivos += 1
            if tiene_enfermedad:
                positivos_y_enfermos += 1

    if total_positivos == 0:
        return 0
    return positivos_y_enfermos / total_positivos

resultado_simulacion = simular_test(10000)
print(f"Probabilidad estimada de tener la enfermedad dado que el test fue positivo: {resultado_simulacion:.4f}")

def calculate_probability(iterations):
  for i in range(iterations):
    result = (strategy)
    if result["winner"] == True:
      times_won += 1
  print("probability in " + str(iterations) + " iterations with "+ str(strategy) + " strategy: " +str(times_won) + "/" + str(iterations) + " = " + str(times_won/iterations))
