n = int(input("Enter the number >= 2: "))
if n>=2:
    flag = False
    for d in range(2,n,1):
        if n%d ==0:
            flag = True
            break
    if flag:
        print("not prime")
    else:
        print("prime")
else:
    print("Enter valid number >=2")
