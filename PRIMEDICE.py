# cook your dish here
for t in range(int(input())):
    a,b=map(int,input().split())
    a=a+b 
    flag=0
    for i in range(1,a+1):
        if(a%i==0):
            flag+=1 
    if(flag==2):
        print("Alice")
    else:
        print("Bob")
