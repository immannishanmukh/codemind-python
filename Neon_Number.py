x=int(input())
y=x*x;
s=0
while (y!=0):
    a=y%10
    s+=a
    y=y//10
if(s==x):
    print("Neon Number")
else :
    print("Not Neon Number")