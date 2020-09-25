n=int(input("How many terms: "))
a=0
b=1
count=0
if n<=0:
   print("Enter positive ")
else:
    print("Fibonacci sequece:")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
print(end=" ")
