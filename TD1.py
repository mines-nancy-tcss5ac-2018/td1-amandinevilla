f= open('p022_names.txt', 'r')

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

assert digits(1000)

#probleme22


def names():
    T=[]
    Triee=[]
    nombre1=0
    sol=0
    s=0
    for ligne in f:
        L= ligne.split(',')
        for x in L:
            T.append(x[1:len(x)-1])
        Triee=sorted(T)
        i=0
        for x in Triee:
            i+=1
            nombre2=0
            for k in range(len(x)):
                nombre1=i
                nombre2= nombre2 + ord(x[k])-(ord('a')-1) 
            s=nombre1*nombre2   
        sol+=s
    return sol

assert names()

                
            
            
            
            
            
        