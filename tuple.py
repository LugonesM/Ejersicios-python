#Given an integer,n , and n space-separated integers as input, create a tuple, l , of those  integers. 
#Then compute and print the result of hash(l) .



if __name__ == '__main__':
    n = int(input())
    l = map(int, input().strip().split(" "))
    #map aplica la funcion dada a los parametros de una lista individualmente
    #stip saca los espacios
    #split separa los parametros con espacios o el caracter indicado
    print(hash(tuple(l))) 
