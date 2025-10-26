l=[]
while True:
    c=int(input('''
1 push element
2 pop element
3 peek the last element
4 display
5 exit
    '''))
    if c==1:
        n=int(input("Enter the number: "))
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("stack is empty")    
        else:
            p=l.pop()    
            print(p)
            print(l)
    elif c==3:
        if len(l)==0:
            print("stack is empty")        
        else:
            print("peek the last element: ",l[-1])    
    elif c==4:
        print("display: ",l)        
    elif c==5:
        break    
    else:
        print("invalid number")