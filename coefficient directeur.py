#Trouve les coefficient directeurs d'une droite
import random
def coef_droite(x1,x2,y1=0.0,y2=0.0):
    a = (y2-y1)/(x2-x1)
    b = y1 - a *x1
    return a,b

x,y=coef_droite(1.0,2.0)
print(x,y)