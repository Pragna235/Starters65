# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=0
    for i in arr:
        if(arr.count(i) == 1 or arr.count(i) == 2):
            flag+=1
           
            
        
        
        
    if(flag==len(arr)):
        print("Yes")
    else:
        print("No")
            
