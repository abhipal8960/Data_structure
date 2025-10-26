l=[]
while True:
    c=int(input('''
1 insert element
2 delete element
3 front element display
4 rear element display
5 display 
6 exit
    '''))
    if c==1:
        n=int(input("Enter the element: "))
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("queue is empty")    
        else:
            del l[0]    
            print(l)
    elif c==3:
        if len(l)==0:
            print("queue is empty")        
        else:
            print("front element display: ",l[0])    
    elif c==4:
        if len(l)==0:
            print("queue is empty")        
        else:
            print("rear element display: ",l[-1])    
    elif c==5:
        print("display: ",l)        
    elif c==6:
        break    
    else:
        print("Invalid number")