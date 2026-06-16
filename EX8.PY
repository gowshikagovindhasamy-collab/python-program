n=13456;
def count(n):
    c=0;
    while(n):
        n=n//10;
        c=c+1;
    return(c);
print(count(n));
x=n=1;
s=0;
c=0;
while(n):
    a=n%10;
    s=s+a**c;
    n=n//10;
if(x==s):
        print("armstrong");
else:
        print("Not armstrong");
