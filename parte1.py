import random

options = ["goat1", "car", "goat2"]
doors = []

# Poner aleatoriamente los objetos en las puertas
def arrange_prizes():
  num = random.randint(0,len(options)-1)
  doors.append(options[num])
  options.remove(options[num])


def monty_Hall(strategy):
  results = {}

  # Elijo para cada opcion una puerta
  while len(options) != 0:
    arrange_prizes()
  results["door where is the car"] = doors.index("car")+1

  doors_copy = doors.copy()
  
  # Participante elige primer puerta
  first_door = random.randint(1,3)
  results["first chosen door"] = str(first_door)+ "-" + doors[first_door-1]

  #Conductor elige una puerta
  if doors[first_door-1] == "car":
    doors_copy.remove(doors_copy[first_door-1])
    opened_door = random.randint(1, len(doors_copy))
    results["opened door"] =  str(opened_door)+ "-" + doors_copy[opened_door-1]
    doors_copy.remove(doors_copy[opened_door-1])
    final_answer = doors_copy[0]
    results["second chosen door"] = str(doors.index(final_answer)+1) + "-" + final_answer
  
  elif doors[first_door-1] == "goat1":
    opened_door = "goat2"
    results["opened door"] = str(doors.index(opened_door)+1) + "-" + opened_door

    final_answer = "car"
    results["second chosen door"] = str(doors.index(final_answer)+1) + "-" + final_answer

  else:
    opened_door = "goat1"
    results["opened door"] = str(doors.index(opened_door)+1) + "-" + opened_door

    final_answer = "car"
    results["second chosen door"] = str(doors.index(final_answer)+1) + "-" + final_answer

  # Si no elije cambiar "final_answer" es la primer opcion que eligio
  if strategy == False:
    final_answer = doors[first_door-1]
    results.pop("second chosen door")
  
  # Agrego resultado final
  if final_answer == "car":
    results["winner"] = True
  else:
    results["winner"] = False
  
  # Retorno diccionario con los resultados del concurso
  return results
  


def calculate_probability(iterations,strategy):
  times_won = 0
  for i in range(iterations):
    result = monty_Hall(strategy)
    if result["winner"] == True:
      times_won += 1
  print("probability in " + str(iterations) + " iterations with "+ str(strategy) + " strategy: " +str(times_won) + "/" + str(iterations) + " = " + str(times_won/iterations))


#PARTE 1.1
print("PARTE 1.1")
game_results = monty_Hall(True)
print(game_results)
print(" ")

#PARTE 1.2
print("PARTE 1.2")
calculate_probability(1000, False)
calculate_probability(10000, False)
calculate_probability(100000, False)
print(" ")
calculate_probability(1000, True)
calculate_probability(10000, True)
calculate_probability(100000, True)