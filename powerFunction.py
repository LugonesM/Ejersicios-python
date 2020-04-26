#Read an integer n . For all non-negative integers , print n².
#The first and only line contains the integer,n .
#constrain 0<n<21

if __name__ == '__main__':
    n = int(raw_input())
 
    if n in range(1,20):
     for i in range(0,n):
        print(pow(i,2))
