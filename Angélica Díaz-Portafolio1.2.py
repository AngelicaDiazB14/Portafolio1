#Ejercicio 1
#Nombre: corrimientoAEntero
#Entradas: Un número de punto flotante
#Salidas: convertir el numero a entero incluyendo los decimales
#restricciones: el numero debe ser mayor a cero y flotante positivo



def corrimientoAEntero(num):
     if(isinstance(num,float) and num > 0 ):
          return int (num * corrimientoAEntero_aux(num))
     else:
          return print("El número ingresado debe ser escrito con decimales y debe ser mayor a cero")
     


 
def corrimientoAEntero_aux(num):
     entero = int(num)
     resta = entero - num
     if(resta == 0):
          return 1
     else:
          return 10 * corrimientoAEntero_aux(num * 10)






#___________________________________________________________
#Ejercicio 2
#Nombre: contarDigitosFlotante
#Entradas: un número con decimales positivo o negativo
#Salidas: La cantidad de dígitos que posee el número incluyendo decimales
#restricciones: el número ingresado debe ser decimal positivo o negativo
#En este ejercicio utilicé un llamado a la función "largo" y a "corrimientoAEntero"
def contarDigitosFlotante(num):
     if(isinstance(num,float)):
          if num<0:
               return print (largo(corrimientoAEntero(num*-1)))
          else:
               return print(largo(corrimientoAEntero(num)))
     else:
          return print("Error de entrada, ingrese un número con decimales")
          
    


 
     
#___________________________________________________________
#Ejercicio 3
#Nombre: indiceNumero
#Entradas: num = un número entero positivo >= 0. indice = un número entero positivo mayor o igual a cero 
#Salidas: retornar el numero segun el inidice ingresado
#restricciones: solo numeros enteros positivos, y el indice no debe ser mayor al largo
def indiceNumero(num, indice):
     if isinstance(num, int) and num > 0 :
          l =  largo(num)
          if l > indice :
               return auxiliarIndice(num, indice, l-1)
          else:
               return print("Error: el índice debe ser menor al largo del número") #error en la entrada
     else:
          return print("El número ingresado debe ser entero positivo mayor a cero") #error en la entrada
     
def auxiliarIndice(num, indice, l):
     if indice == l: 
          return num%10
     else:
          return auxiliarIndice(num//10, indice, l-1)
#_______________________________________________________________
#Cuenta la cantidad de dígitos que tiene el número ya sea positivo o negativo, esta la utilizo para el ejercicio 2 y 3
def largo(num):
     if isinstance(num, int):
          if(num >= 0 and num < 10):
               return 1
          elif(num > 10):
               return auxLargo(num)
          elif(num < 0):
               return auxLargo(num*-1)
     else:
          return print("Ingrese un número entero")

     
def auxLargo(num):
     if num == 0:
          return 0
     else:
          return 1+auxLargo(num//10)

#___________________________________________________________
#Ejercicio 4
#Nombre: contarNumero
#Entradas: tres números, el primero será el número a cortar y los otros dos serán los índices (i1, i2).
#Salidas: retornar el nuevo número según sus índices
#restricciones: solo se permiten números enteros positivos  mayores o iguales a cero
#En este erjercicio haré un llamado a mi función anterior "indiceNumero".

def cortarNumero(num, i1, i2):
     if(isinstance(num,int) and isinstance(i1,int) and isinstance(i2,int)):
          if(num >= 0 and i1 >= 0 and i2 >= 0):
               i1 = indiceNumero(num,i1)
               i2 = indiceNumero(num,i2)
               return cortarNumero_aux(i1, i2)
          else:
               return print("Los números ingresados deben ser positivos")
     else:
          return print("Los tres números a ingresar deben ser enteros")

def cortarNumero_aux(i1, i2):
     if(i2 == 0):
          return 0
     else:
          return i1*10 + i2 + cortarNumero_aux(i1,i2 // 10)









     


