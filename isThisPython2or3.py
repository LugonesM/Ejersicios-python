



#In Python 2, when you divided one integer by another integer, no matter what, the result would always be an integer.
#In order to make this a float division, you would need to convert one of the arguments into a float.
#Since Python doesn't declare data types in advance, you never know when you want to use integers and when you want to use a float. Since floats lose precision, it's not advised to use them in integral calculations.
#To solve this problem, future Python modules included a new type of division called integer division given by the operator //.

#Now, / performs float division, and // performs integer division

if __name__ == '__main__':
    
print(" Using two intergers to know if you are in python 2 or 3..........")
    
a = 100
b = 23
c = (a/b)

if type(c) == int :
    print(" You are in Pyton 2.7 or older ")
    print(" To use / vs // correctly you need to put : <<from __future__ import division>> at beguining of file")
    print(" Without it, when you divide two \" ints \" the result is always another \" int \" ")
    
    print(" And "+ str(a) + " / " + str(b) + " = " + str(a//b))   
    print(" And "+ str(a) + " // " + str(b) + " = " + str(a/b))   
    
    z = float(a)
    
    print(" But in python 3 : "+ str(a) + " / " + str(b) + " = " + str(z/b))
    print(" And "+ str(a) + " // " + str(b) + " = " + str(z//b))
   
else:
   print(" You are in Pyton 3 ")
   answer1 = " Here division works like : {} / {} = {}"  
#in python3 you can print strings and intergers using function format() like this
    
   print(answer1.format(a,b, (a/b)))
   print(" And "+ str(a) + " // " + str(b) + " = " + str(a//b))  
#Or you can use function str() to convert the intergers into strings or use comas like:
# print("suma de", i, "con ", z," : ", sum)

 
