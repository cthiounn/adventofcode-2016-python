import re


with open("input3.txt") as toto:
    malist=toto.readlines()

# 783  255  616
def triangle(uncote, deuxiemecote,troisiemecote):
    resa=uncote+deuxiemecote
    resb=uncote+troisiemecote
    resc=deuxiemecote+troisiemecote
    if resa>troisiemecote and resb>deuxiemecote and resc>uncote:
        return 1
    else:
        return 0

def fairepartie1(uneliste):
    somme=0
    for i, nombre in enumerate(malist):
        x,y,z = re.split(r'\W+',nombre.strip())
        somme+=triangle(int(x),int(y),int(z))
    print(somme)

def lineariser(uneliste):
    malist=[]
    malist2=[]
    malist3=[]
    for i, nombre in enumerate(uneliste):
        x,y,z = re.split(r'\W+',nombre.strip())
        malist.append(x)
        malist2.append(y)
        malist3.append(z)
    malist.extend(malist2)
    malist.extend(malist3)

    somme=0
    while len(malist)!=0:
        x=malist.pop(0)
        y=malist.pop(0)
        z=malist.pop(0)
        somme+=triangle(int(x),int(y),int(z))
    print(somme)

fairepartie1(malist)
lineariser(malist)