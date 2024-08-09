"""
Instrucciones de tareas:
solicitar al usuario dos valores y determinar cual numero es el mayor
solicitar al usuario dos valores:
number1:(int)
number2:(int)
se debe imprimir el mayo de los dos numeros(la salidad debe ser identica a la que sigue):

Proporcion el numero 1:
proporciona el numero2:
el numero mayor es <numeromayor>
"""
number1 = int(input('Proporciona el numero 1: '))

number2 = int(input('proporciona el numero 2: '))

if number1>number2:
    print (f'el numero mayor es:  {number1} ')
else:
    print (f'el numero mayor es: {number2} ')