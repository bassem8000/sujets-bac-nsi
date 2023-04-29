def multiplication(n1,n2):
    '''renvoie le produit de n1 par n2 supposés entiers relatifs'''
    cpt = 0
    if n1 == 0 or n2 == 0:
        return 0
    elif n1 < 0 :
        return -multiplication(-n1,n2)
    elif n2 < 0 :
        return -multiplication(n1,-n2)
    for i in range(n1):
        cpt = cpt + n2
    return cpt


assert multiplication(-2,6) == -12
assert multiplication(3,5) == 15
assert multiplication(-4,-8) == 32
assert multiplication(-2,0) == 0






def chercher(tab, n, i, j):
    '''cherche'''
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m
    
def recherche_indices_classement(elt,tab):
    min = []
    eg =  []
    max = []
    for i in range(len(tab)):
        if elt > tab[i]:
            min.append(i)
        elif elt < tab[i]:
            max.append(i)
        else:
            eg.append(i) 
    return(min,eg,max)

def recherche(n,tab):
    cpt = 0
    for elt in tab:
        if n == elt:
            cpt +=1
    return cpt

def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i] > tab[i+1]:
            return False
    return True

print(verifie([5]))


