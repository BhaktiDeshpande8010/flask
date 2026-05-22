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
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("not a prime number")

# else:
#     for i in range(2,num):
#         if num % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")
        

list1=["Apple","Banana","Rohan",345.6,"friend"]
print(list1)
print(type(list1))

list1.append("temp")
print(list1)

# take 6 input from user and store in list 
fruit=[]
f1 = input("Enter Fruit name :")
fruit.append(f1)
f2 = input("Enter Fruit name :")
fruit.append(f2)
f3 = input("Enter Fruit name :")
fruit.append(f3)
f4 = input("Enter Fruit name :")
fruit.append(f4)
f5 = input("Enter Fruit name :")
fruit.append(f5)

print(fruit)