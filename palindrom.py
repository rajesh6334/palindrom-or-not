#palindrom
n=int(input())
temp=n
r=0
while(n>0):
    
    remainder=n%10
    r=r*10+remainder
    n=n//10
if r==n:
    print(palindrom)
else:
    print('not palindrom')
