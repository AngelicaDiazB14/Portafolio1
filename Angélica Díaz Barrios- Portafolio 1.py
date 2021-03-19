"""
Esta función nos permite saber cuáles son los divisores de un número entero positivo
mayor que cero , mostrando los dígitos divisores del mayor al menor.

Nombre:
      divisorNum
Entradas:
         n: un número entero positivo mayor a cero
Salidas:
        el retorno de los divisores de forma descendente del número ingresado inicialmente.
Restricciones:
              El número debe ser entero positivo mayor a cero.
"""

def divisores(num):
    divisor=num
    if(isinstance(num,int) and (num > 0)): #Validando que el número sea entero positivo > a 0
        return divisores_aux(num, divisor)
    else:
        return print("Error: ingrese un número entero positivo mayor que cero")

def divisores_aux(num, divisor):#Función auxiliar que incluye otros parámetros,los cuales no son solicitados al usuario
    residuo = num % divisor
    if(divisor == 1):
        return 1
    elif(residuo == 0):
        print(divisor)
        return divisores_aux(num, divisor - 1)
    elif(residuo != 0):
        return divisores_aux(num, divisor - 1)
#-----------------------------------------------------------------------------------------------------------------------    

"""
Esta función nos permite un número "n" por un número "m" sin utilizar el operador de multiplicación

#Nombre:
        multiplicarRecursivo
#Entradas:
        num: un número entero mayor o menor a cero, es decir, puede ser negativo
        factor: un número entero positivo mayor o igual a cero
#Salida:
        el resultado de multiplicar num por el factor,
        es decir el producto de esa multiplicación
#Restricciones:
            los números ingresados deben ser enteros y el factor debe ser positivo
            no se puede utilizar el signo de multiplicación.
"""

def multiplicarRecursivo(num, factor):
    if(isinstance(num, int) and isinstance(factor,int) and factor >= 0):
        print("El resultado de su multiplicación es:")
        return multiplicarRecursivo_aux(num, factor)
    else:
        return print("Error: solo se permiten números enteros y el segundo dígito(factor) no puede ser negativo")

def multiplicarRecursivo_aux(num, factor):
    if(factor == 0):
        return 0
    elif(factor == 1):
        return num
    elif(factor > 1):
        return num + multiplicarRecursivo_aux(num, factor -1)
    elif(num < -1):
        return num + multiplicarRecursivo_aux(num, factor -1)
    
#------------------------------------------------------------------------------------------------------------------
"""
Esta función permite resolver una división entera dado un número n entre un número m sin utilizar
el operador de división.

Nombre:
      divisionRecursivo
Entradas:
        divisor: primer número que se deberá ingresar que sea entero positivo mayor a cero
        dividendo: segundo número a ingresar que sea entero positivo mayor a cero
Salidas:
        El resultado de la división entera
Restricciones:
             Ambos dígitos deben ser enteros positivos mayores a cero
"""

def divisionRecursivo(divisor, dividendo):
    if(isinstance(divisor, int) and divisor > 0 and isinstance(dividendo, int) and dividendo > 0):
        print("El resultado de su división es: ")
        return divisionRecursivo_aux(dividendo, divisor)
    else:
        return print("Error: debe ingresar números enteros positivos mayores a cero")

def divisionRecursivo_aux(dividendo, divisor):
    if(dividendo == 0):
        return 0
    elif(dividendo < 0):
        return -1
    else:
        return 1+divisionRecursivo_aux(dividendo-divisor, divisor)







    





















    
    



