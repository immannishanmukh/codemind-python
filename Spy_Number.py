x=int(input())
s=0
p=1
while x!=0:
    d=x%10
    s=s+d
    p=p*d
    x=x//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")