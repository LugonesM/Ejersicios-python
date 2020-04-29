#list comprehensions:
#You are given three integers X,Y and Z  representing the dimensions of a cuboid along with an N integer .
#You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (x+y+z) is not equal to N.
#Here: 0<=i<=X;0<=j<=Y;0<=k<=Z;
#Input format: Four integers  and  each on four separate lines, respectively
#sample output : [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

import sys 
def check( value ) :   #funcion que chequea que el usuario ingreso valores posibles para la cuenta 
 try:
  int(value)
 except ValueError:  #de no ser asi imprime un mensaje de error y sale del programa
   print( "pone solo numeros")
   sys.exit()
 return #si la cadena se pudo convertir retorna 1
 
def pasaAint( cadena ):   #convierte cadena en int
 if type(cadena) == str :
   if check(cadena) != 1 :
     cadena=int(cadena)+1   #suma 1 para usar la funcion range correctamente
 return cadena


if __name__ == '__main__':
    x = input()    # con x=(int(input()) es mas sensillo, pero de no poner solo numeros, el programa se traba 
    x = pasaAint(x)  #esta funcion se asegura de convertir el input en int, si no, sale de programa
    y = input()
    y = pasaAint(y)
    z = input()
    z = pasaAint(z)
    n = input()
    n = pasaAint(n)

    lista = []
    for i in range (0,x):
        for j in range (0,y):
            for k in range (0,z):
                if (i+j+k) != n :
                    lista.append([i,j,k])
                    
    print(lista)
    
sys.exit()
