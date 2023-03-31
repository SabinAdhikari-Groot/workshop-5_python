n1, n2 = 0, 1
num = int(input("Enter any number:"))
print(n1)
for i in range(1,num):
    sum=n1+n2
    n1=n2
    n2=sum
    print(n1)
