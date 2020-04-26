import sys 
#Read an integer n.
#Without using any string methods, try to print the following: 123...n
#The first line contains an integer n .

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
     print(i, end="") #this way it prints everything in the same line

sys.exit()
