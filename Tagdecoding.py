tag=input()
v='AEIOUY'
n='123456789'
i,flag=0,0
while i<len(tag)-1:
    #print(i)
    if (n.find(tag[i])>-1 and n.find(tag[i+1])>-1):
        if ((int(tag[i])+int(tag[i+1])) % 2) == 0:
            falg=1
        else:
            flag=2
            #print('first break')
            break
    elif n.find(tag[i]) > -1 and v.find(tag[i+1])==-1 and i>0 :
        flag=1
    elif v.find(tag[i])== -1 and n.find(tag[i+1])>-1 and i<7 :
        flag=1
    elif v.find(tag[i])==-1 and v.find(tag[i+1])==-1:
        flag=1
    else:
        flag=2
        #print('last break')
        break
    i+=1
if flag==1:
    print('valid')
else:
    print('invalid')
