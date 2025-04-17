# Tarea1_PYE
  A continuación se detallará la letra del proyecto 1 correspondiente a la materia Probabilidad y Estadística Aplicada, realizado por los alumnos Julián Bevc, Paulina Vidal y Belén Tellechea. Puedes observar el informe acerca de este en el siguiente enlace: https://docs.google.com/document/d/1grCinA0ERapIPdORldC4URf0q63vgEDOwi8Z9jcYV80/edit?usp=sharing. 

## Parte 1: Problema de Monty Hall
  El problema de Monty Hall es un problema de probabilidad inspirado en un viejo concurso de televisión llamado “Let’s Make a Deal”. El problema consiste en que un concursante tiene delante tres puertas, detrás de una de ellas hay un auto nuevo y en las otras dos hay cabras, el concursante debe adivinar en cuál puerta está el vehículo.
  Sin embargo, una vez el concursante elige una de las puertas, Monty Hall (El presentador que sabe que hay detrás de cada puerta) abre una de las puertas donde haya una cabra (si las dos puertas no elegidas por el concursante tienen una cabra, Monty Hall abre una al azar) y le da la opción al concursante de cambiar la puerta que eligío por la otra puerta que está cerrada. Por ello podríamos preguntarnos: ¿Cambiar de puerta puede influir en las chances del concursante de ganar el auto?
1.  Escriba una función en Python que simule el problema de Monty Hall. La funció deberá recibir como parámetro un booleano que indique la estrategia elegida por el jugador, TRUE indica que el participante cambiará de puerta, FALSE indica que el partipante no cambiará de puerta. La función debe imprimir en pantalla los resultados de la simulación
- Puerta elegida por el participante.
- Puerta donde está el auto.
- Puerta abierta por el presentador.
- En caso de cambio de puerta indicar cual es la nueva puerta que elige el participante.
- Resultado del concurso (el participante gana o no gana el auto).

  Se recomienda usar la función randint de la librería random para la generación de los números aleatorios necesarios para la implementación de esta función.
2. Ejecutar la función 1.000, 10.000 y 100.000 veces para la estrategia de cambio de puerta y cuente la cantidad de veces que el juego resulta en que el participante gana el auto. Repita esta parte para la estrategia donde no se cambia la puerta.
3. ¿Cuánto vale la probabilidad empírica de que el participante gane el auto con la estrategia de cambio de puerta? ¿Cuánto vale la misma probabilidad con la estrategia donde no se cambia la puerta? ¿Alguna de las dos estrategias es preferible?
4. Buscar información sobre el problema. En particular buscar alguna explicación sobre lo observado al comparar ambas estrategias.

## Parte 2: Problema del cumpleaños 
  El problema del cumpleaños consiste en un juego que realizan m personas donde el objetivo es detectar si al menos dos personas del grupo tienen el mismo día del año como fecha de cumpleaños.
  Para modelar este problema asumiremos que hay equiprobabilidad entre los 365 días del año, y que nadie cumple años un 29 de febrero.
  Para la cantidad de personas, se trabajará con los valores m = 10, m = 20, m = 30, m = 40 y m = 50.
1. Escriba una función en Python que simule el problema del cumpleaños. La función deberá recibir como parámetro la cantidad de personas que jugarán el juego, y devolver un booleano que indique la victoria o la derrota en el juego.
2. Ejecutar la función 1.000, 10.000 y 100.000 veces para cada uno de los valores de m especificados. Registrar la cantidad de victorias y derrotas en cada caso.
3. Para cada valor de m especificado, calcular empíricamente la probabilidad de ganar el juego. ¿Eran esperables estos resultados?
4. Calcular la probabilidad teórica de ganar el juego para cada valor de m especificado, y comparar con las probabilidades empíricas obtenidas.

## Parte 3: Problema de la enfermedad
  Se sabe que una cierta enfermedad afecta a 1 de cada 10.000 personas en la población. Se ha diseñado un test que permite detectar si una persona tiene la enfermedad. El test es bastante preciso. En particular se sabe que
- La probabilidad de que el test de positivo (sugiriendo que la persona tiene la enfermedad), dado que la persona no tiene la enfermedad, es de 0,02. Esto se conoce como un falso positivo.
- La probabilidad de que el test de negativo (sugiriendo que la persona no tiene la enfermedad), dado que la persona si tiene la enfermedad, es de 0,01. Esto se conoce como un falso negativo.
  Se elige una persona al azar en la población y se le aplica el test. El resultado es positivo. Se desea calcular la probabilidad de que efectivamente la persona tenga la enfermedad.
1. Modele e implemente en Python una simulación que permita estimar de forma empírica la probabilidad pedida.
2. Calcular de forma exacta la probabilidad pedida y comparar con el resultado de la simulación.
3. ¿Es el resultado el esperado si nos basamos en nuestra intuición? ¿Puede explicar por qué?
