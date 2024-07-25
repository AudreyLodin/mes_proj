
def est_amicaux(N,N1):
    somme=0
    somme1=0
    for n in range(1,N):
        if N%n == 0:
            somme=somme+n

    for n1 in range(1,N1):
        if N1%n1 == 0:
            somme1=somme1+n1
    if somme==N1 and somme1==N:
        return True
    else :
        return False

m=int(input("Entrez un premier nombre : \n"))
m1=int(input("Entrez un second nombre : \n"))
n=est_amicaux(m,m1)
print(n)