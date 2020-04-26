#Read an integer n . For all non-negative integers , print n².
#The first and only line contains the integer,n .
#constrain 0<n<21

if __name__ == '__main__':
    n = int(raw_input())
 
    if n in range(1,20):
    #En Python 2, range() se consideraba una función, pero en Python 3 no se considera una función, sino un tipo de datos , aunque se utiliza como si fuera una función.
     for i in range(0,n):
        print(pow(i,2))
