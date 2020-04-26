import sys 
#Given a range of first 10 numbers, Iterate from start number to the end number 
#and print the sum of the current number and previous number


def suma(num):
    antNum = 0
    for i in range(num):
        sum = antNum + i
        print("suma de (actual)", i, "con (anterior)", antNum," : ", sum)
        antNum = i

print("siguiendo una lista de 10 numeros en orden, imprimiendo la suma del anterior con el actual: ")
suma(10)

sys.exit()
