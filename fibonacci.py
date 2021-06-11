s=int(input("Enter a number:"))
n1,n2,i=0,1,0
if s<=0:
    print("Please enter a positive integer")
elif s==1:
    print(n1)
else:
    while i<=s:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        i+=1
