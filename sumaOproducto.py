#Accept two integer numbers from a user and return their product 
#if the product is greater than 1000, then return their sum

import sys 

def multiplicationOsuma(n1, n2):
  mult = n1* n2
  if(mult <= 1000):
    return mult
  else:
    return n1 + n2


num1 = int(input("Primer numero "))
num2 = int(input("Segundo numero "))

result = multiplicationOsuma(num1, num2)
print("Resultado : ", result)

sys.exit()
