# n = 4
# for i in range(1, n + 1):
#     print('*' * i)


# num =int(input("Enter a number :"))
# for i in range(1 ,num +1):
#    print('*' *i)


# a =int(input("Enter a number :"))
# for i in range(1,11):
#    print(a, "x", i, "=", a * i)

# p=4
# for i in range(1, p+1):
#    print(str(i)*i)


# prim number
num = int(input("Enter a number: "))

if num <= 1:
    print("not a prime number")

else:
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")