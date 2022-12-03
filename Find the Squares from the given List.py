a=[]
n=int(input("enter the how many values in the list :"))
for i in range(n):
    b=int(input('enter a value:'))
    a.append(b)
def square(x):
   return x**2
print(list(map(square,a)))    
