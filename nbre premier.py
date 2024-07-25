from math import sqrt

def nbre_premier(N):
    #u=sqrt(N)
    if N ==1 or N == 0:
        return False
    if N % 2 != 0:
        """
        if N%u != 0:
        return True
        """
        for n in range(2,N-1) :

            if N%n == 0:
                return False

        return True
    else :
        return False

m=0
while m != -1:
    m = int(input("Entrez un nombre entier : \n"))
    n=nbre_premier(m)
    print(n)