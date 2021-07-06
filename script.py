with open('input1.in') as myfile:
    mylist=[line.split(',') for line in myfile][0]

print(myfile)
print(mylist)

pos= (0,0)
direction = ('N','E','O','S')
madirection='N'


#R  => E  , L => O
malist=[]
mondico={}
for i,element in enumerate(mylist):
    # print(i,element.strip())
    ordre=element.strip()
    lettre=ordre[0]
    cases=ordre[1:]


    # print(lettre)
    
    # print(madirection)
    if 'L' == lettre:
        if madirection=='N':
            madirection='O'
        elif madirection=='O':
            madirection='S'
        elif madirection=='S':
            madirection='E'
        elif madirection=='E':
            madirection='N'
    elif 'R' == lettre:
        if madirection=='N':
            madirection='E'
        elif madirection=='E':
            madirection='S'
        elif madirection=='S':
            madirection='O'
        elif madirection=='O':
            madirection='N'

    # print(madirection)
    # if i>3:
    #     break
    # print(cases)

    # print(pos)
    cases=int(cases)
    # print(type(pos[0]))

    for _ in range(cases):
        if madirection=='N':
            pos=(pos[0],pos[1]+1)
        elif madirection=='O':
            pos=(pos[0]-1,pos[1])
        elif madirection=='S':
            pos=(pos[0],pos[1]-1)
        elif madirection=='E':
            pos=(pos[0]+1,pos[1])
 
        if pos in mondico:
            mondico[pos]+=1
            print("COUCOU AKMAT",pos)
            break
            
        else:
            mondico[pos]=1

print(mondico)
print(pos)
# for i,e in enumerate(malist):
#     nombrefoisvisite=malist.count(e)

#     if nombrefoisvisite>1:
#         print(e,malist.count(e))
# print(malist)
    # print(pos)
    # break
# def toto(variable):
    # malist=[]
    # malist.append(variable)
    # malist.append("mario")
    # malist.append("mario")
    # malist.append("bowser")
    # print(malist)
    # malist2=malist.copy()
    # malist.reverse()
    # print("tptp",malist) 
    # print("t",malist2)
    # malist.clear()


    # mondico=dict()
    # #mondico={}
    # mondico["Inkling"]="Yowai"
    # mondico["Palutena"]=["Sugoi","Strong"]

    # print(mondico)
    # print(mondico["Inkling"][1])
    # print(malist) 

    # for i in range(len(malist)):
    #     print(i,malist[i])

    # for i,element in enumerate(malist):
    #     print(i,element)


    # print(malist[0])
    # var1,var2,var3=malist
    # print(malist)
    # print(var1)
    # print(var2)
    # print(var3)
    # print("coucou {}, tu es un bébé {}".format(var1,var2))

# toto("akmat")