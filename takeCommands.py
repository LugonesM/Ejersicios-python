#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

#Initialize your list and read in the value N of  followed by N lines of commands where each command will be of the  types listed above. 
#Iterate through each command in order and perform the corresponding operation on your list.
#The first line contains an integer, N, denoting the number of commands.
#Each line i of the n subsequent lines contains one of the commands described above
if __name__ == '__main__':
    n = int(input())
    l =[]
    for _ in range(n):
        s=input().split()
        comando=s[0]
        args=s[1:]
        if comando !="print":
            comando += "("+",".join(args) +")"
            eval("l."+comando)
        else:
            print(l)


