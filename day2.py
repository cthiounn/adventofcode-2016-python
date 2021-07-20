with open("input2.txt") as toto:
    malist=toto.readlines()


def bouge(commande, point):
    x,y = point
    if commande=='L':
        if x>=0:
            x-=1
    elif commande=='R':
        if x<=0:
            x+=1
    elif commande=='U':
        if y<=0:
            y+=1
    elif commande=='D':
        if y>=0:
            y-=1
    # return (-1,0)
    return (x,y)

def chiffre(point):
    if point==(0,0):
        return 5
    if point==(1,0):
        return 6
    if point==(0,1):
        return 2
    if point==(1,1):
        return 3
    if point==(-1,0):
        return 4
    if point==(0,-1):
        return 8
    if point==(-1,1):
        return 1
    if point==(-1,-1):
        return 7
    if point==(1,-1):
        return 9


def fairepartie1(malistvar):
    o=(0,0)
    for i,ligne in enumerate(malistvar):
        for j, caractere in enumerate(ligne):
            o=bouge(caractere,o)
        print(o, chiffre(o))


#fairepartie1(malist)
assert(bouge('L',(1,0))==(0,0))
assert(bouge('L',(0,0))==(-1,0))
assert(bouge('L',(-1,0))==(-1,0))
assert(bouge('R',(1,0))==(1,0))
assert(bouge('R',(0,0))==(1,0))
assert(bouge('R',(-1,0))==(0,0))

assert(chiffre((-1,0))==4)

#bouge L -1 0  => -1 0
#BOUGe L 0 0 => -1 0
#bouge  L 1 1 => 0 1
# bouge L -3 1 => -1 1

def bouge2(commande, point):

    x,y = point
    if commande=='L':
        if chiffre2((x-1,y))!=999:
            x-=1
    elif commande=='R':
        if chiffre2((x+1,y))!=999:
            x+=1
    elif commande=='U':
        if chiffre2((x,y+1))!=999:
            y+=1
    elif commande=='D':
        if chiffre2((x,y-1))!=999:
            y-=1
    # return (-1,0)
    return (x,y)

def chiffre2(point):
    if point==(0,0):
        return 7
    if point==(1,0):
        return 8
    if point==(0,1):
        return 3
    if point==(1,1):
        return 4
    if point==(-1,0):
        return 6
    if point==(0,-1):
        return "B"
    if point==(-1,1):
        return 2
    if point==(-1,-1):
        return "A"
    if point==(1,-1):
        return "C"
    if point==(2,0):
        return 9
    if point==(-2,0):
        return 5
    if point==(0,-2):
        return "D"
    if point==(0,2):
        return 1
    return 999


def fairepartie2(malistvar):
    o=(-2,0)
    for i,ligne in enumerate(malistvar):
        for j, caractere in enumerate(ligne):
            o=bouge2(caractere,o)
        print(caractere,o, chiffre2(o))


fairepartie2(malist)