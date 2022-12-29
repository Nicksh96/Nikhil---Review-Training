n = int(input("Enter no: "))
n1, n2 = 0, 1
if n<=0:
    print("Enter valid no.")
elif n==1:
    print("Fibonacci Series:",n1)
elif n==2:
    print("Fibonacci Series:", n1, n2)
else:
    print("Fibonacci Series:", n1, n2, end=" ")
    for i in range(2,n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
