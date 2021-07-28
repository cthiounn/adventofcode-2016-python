import re

with open("input4.txt") as tontonestnulasmash:
    liste=tontonestnulasmash.readlines()


def test(nom, id, check):
    #si c'est vrai, on renvoie id
    if testsiegal(nom,check):
        return id
    # sinon on renvoie 0
    else:
        return 0

def takeFirst(elem):
    return elem[0]
def takeSecond(elem):
    return elem[1]

def testsiegal(nom,check):
    mondict={}
    for i,j in enumerate(nom):
        # si la lettre j n'est pas le dictionnaire, on rajoute  la lettre j et le compteur à 1
        if j!="-":
            if j not in mondict :
                mondict[j]=1
            # sinon, la lettre est dedans, et on incrémente le compteur
            else:
                mondict[j]+=1
    masuperliste=list(mondict.items())
    masuperliste.sort(key=takeFirst)
    masuperliste.sort(key=takeSecond, reverse=True)

    monresultat=""
    for i,j in enumerate(masuperliste[0:5]):
        a,b=j
        monresultat+=a


    if (check==monresultat):
        return True
    else:
        return False
 

 
masomme=0
for i,j in enumerate(liste):
    regex=re.compile("(.*)-([0-9]{3})\[([a-z]{5})\]")
    resultat=regex.findall(j)
    a,b,c=resultat[0]
    masomme+=test(a,int(b),c)
print(masomme)