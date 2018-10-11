#probleme 16

def digits(n):
    s=2
    reste=0
    sol=0
    for i in range(1,n):
        s=s*2    #calcul de 2*1000
    nombre=s
    while nombre!=0:
        reste=nombre%10
        quo=nombre//10   #decomposition en base 10
        sol+=reste
        nombre=quo
    return sol

#Probleme 22
f= open('Users/amandinevilla/Desktop/p022_names.txt','r')

def conversion(mot):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    M=mot
    s=0
    L=[]
    for k in range(len(M)):
        i=0
        j=False
        while j== False:
            if M[k]==alphabet[i]:
                j=True
                s+=i+1
            i+=1
    return s
    
    
def names():
    Triee=[]
    sol=0
    s=0
    for ligne in f:
        L= ligne.split(',')
        Triee=sorted(L)
        i=0
        for x in Triee:
            i+=1
            s=i*conversion(x)
            sol+=s
    return sol
    
#Probleme55

def retourne(k):
    y=0
    while k!=0:
        reste=k%10
        quotient=k//10
        y=y*10+reste
        k=quotient
    return y 

def palynd(k):
    L=[]
    while k!=0:
        reste=k%10
        quotient=k//10
        k=quotient
        L.append(reste)        #test d'une première fonction trop compliquée
    for i in range(len(L)):
        if L[i]!=L[len(L)-i-1]:
            return False
        else :
            return True

def palyndrome(n):
    a=str(n)
    b=a[::-1]
    return a==b


def lychrel(n):
    i=0
    while i<50:
        n=n+retourne(n)
        if palyndrome(n):
            return False
        i+=1
    return True


  
def compteur():
    s=0
    for i in range(10001):
        if lychrel(i):
            s+=1
    return s 