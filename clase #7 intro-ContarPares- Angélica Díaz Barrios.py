"""
nombre: numeroPar
Entrada: un número
Salida: True si es un número par o False si no lo es.
Restricciones: el numero debe ser entero positivo
"""
"""
nombre: numeroPar
Entrada: un número
Salida: True si es un número par o False si no lo es.
Restricciones: el numero debe ser entero positivo
"""

                           
def numeroPar(num):
    if(num%2==0):
        return True
    else:
        return False


    
"""
nombre: cantidadNumerosPar
Entrada: un número mayor o igual a cero
Salidad: la cantidad de pares que tiene el número ingresado
Restrincción: el número debe ser entero positivo
"""

def cantidadNumerosPar(num):
    if(isinstance(num,int) and (num >= 0)):
        if(num == 0):
            return 1
        else:
            return cantidadNumerosPar_aux(num)
    else:
        return ("Error: debe ingresar un número entero positivo")

def cantidadNumerosPar_aux(num):
    if(num == 0):
        return 0
    elif(num%2==0):
        return 1+cantidadNumerosPar_aux(num//10)
    else:
        return 0+cantidadNumerosPar_aux(num//10)
