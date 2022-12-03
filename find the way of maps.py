a=[]
n=int(input("enter the how many values in the list"))
for i in range(n):
    b=int(input('enter a value:'))
    a.append(b)
def triple(x):
   return x*3
print(list(map(triple,a)))    
