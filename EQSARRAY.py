# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    p=arr.count(k)
    if(p==0):
        print("No")
    elif(p==1 and n!=1 and arr[n-1]==k):
        print("No")
    else:
        print("Yes")
                
            