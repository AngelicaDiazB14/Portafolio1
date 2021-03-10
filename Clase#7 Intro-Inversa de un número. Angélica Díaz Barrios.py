"""
Nombre: cantidadDigitos
Entrada: un número mayor o igual a cero
Salidad: cantidad de dígitos que posee el numero ingresado.
Restrincción: el número debe de ser entero positivo
"""

def cantidadDigitos(num):
    if(isinstance(num,int) ==False):
        return print("Error: tipo de dato no es un número entero")
    elif (num ==0):
        return 1
    else:
        return cantidadDigitos_aux(num)

    
def cantidadDigitos_aux(n):
    if(n ==0):
        return 0
    else:
        return 1 + cantidadDigitos_aux(n // 10)
    
        
"""
Nombre: inversaNum
Entrada: número mayor o igual a cero
Salida: el número inverso del número ingresado originalmente con todos sus dígitos.
Restrinccione: el número debe ser entero positivo mayor o igual a cero
"""


def inversaNum(num):
    if isinstance(num, int):
        if (num >= 0):
            if (num <= 10):
                return num
            else:
                return inversaNum_aux(num, cantidadDigitos(num))
        else:
            print ("Error: elnúmero ingresado debe ser positivo") 
    else:
        print ("Error: debe ingresar un número entero positivo")


def inversaNum_aux(num, largo):
    if largo == 0:
        return 0
    else:
        return (num % 10) * (10 ** (largo - 1))+ inversaNum_aux(num // 10, largo - 1)
