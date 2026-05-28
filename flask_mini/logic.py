# # n = 4
# # for i in range(1, n + 1):
# #     print('*' * i)


# # num =int(input("Enter a number :"))
# # for i in range(1 ,num +1):
# #    print('*' *i)


# # a =int(input("Enter a number :"))
# # for i in range(1,11):
# #    print(a, "x", i, "=", a * i)

# # p=4
# # for i in range(1, p+1):
# #    print(str(i)*i)


# # # prim number
# # num = int(input("Enter a number: "))

# # if num <= 1:
# #     print("not a prime number")

# # else:
# #     for i in range(2,num):
# #         if num % i == 0:
# #             print("Not prime")
# #             break
# #     else:
# #         print("Prime")
        

# # list1=["Apple","Banana","Rohan",345.6,"friend"]
# # print(list1)
# # print(type(list1))

# # list1.append("temp")
# # print(list1)

# # # # take 6 input from user and store in list 
# # fruit=[]
# # f1 = input("Enter Fruit name :")
# # fruit.append(f1)
# # f2 = input("Enter Fruit name :")
# # fruit.append(f2)
# # f3 = input("Enter Fruit name :")
# # fruit.append(f3)
# # f4 = input("Enter Fruit name :")
# # fruit.append(f4)
# # f5 = input("Enter Fruit name :")
# # fruit.append(f5)

# # print(fruit)

# # # dictonary / set 
# # words = {
# #     "madat": "help" ,
# #     "khursi" : "chair",
# #     "billi" : "cat"
# # }

# # word = input("Enter a name you want the meaning of : ")

# # print(words[word])

# # s = set()
# # s.add(18)
# # s.add("18")

# # print(s)
# # print(type(s))


# # # //problem 6
# # d = {}

# # name=input("Enter your name :")
# # lang=input("Enter language name :")
# # d.update({name:lang})

# # name=input("Enter your name :")
# # lang=input("Enter language name :")
# # d.update({name:lang})

# # name=input("Enter your name :")
# # lang=input("Enter language name :")
# # d.update({name:lang})

# # name=input("Enter your name :")
# # lang=input("Enter language name :")
# # d.update({name:lang})

# # print(d)



# # CHAPTER-6 // CONDISTIONAL STATEMENT 

# a = int(input("Enter your age :"))

# if(a >= 18):
#     print("you are eligible")
    
# elif(a < 0):
#     print("veda ahes ka...!!")
    
# else:
#     print("Not eligible")
    
# print("End of the program")


# # find largest 
# a =int(input("Enter a number"))
# b =int(input("Enter a number"))

# if (a>b) :
#     print("The greater number is", a )
    
# else:
#     print("The greater number is", b)
    
    
# #negative no
# num =int(input("Enter a Number :"))
 
# if num > 0:
#     print("positive number")
 
# elif num == 0:
#     print("Its an zero")
    
# else:
#     print("Negative number")


# i = int(input("Enter a number"))
# # i=5
# for i  in range(1 , i+1 ):
#     print(i)
    
    
# a = 5
# total = 0

# for i in range(1, a + 1):
#     total = total + i

# print("Sum of the numbers:", total)


# Multiplication Table
# n=3
# for i in range (1,11):
#     print(n, "x" ,i ,"=", i*1)
# print("-----------")

# m=15
# for i in range(1,11,2):
#     print(m ,"x",i,"=",i*1)

# print("-------------")

# age=19
# if(age >= 18):
#     print("yes")

# else:
#     print("no")
    
    
# find greatest of 4 numbers given by user

a1 = int(input("Enter number 1 : "))
a2 = int(input("Enter number 2 : "))
a3 = int(input("Enter number 3 : "))
a4 = int(input("Enter number 4 : "))

if(a1 >= a2 and a1 >= a3 and a1 >= a4):
    print("a1 is greatest :", a1)

elif(a2 >= a1 and a2 >= a3 and a2 >= a4):
    print("a2 is greatest :", a2)

elif(a3 >= a1 and a3 >= a2 and a3 >= a4):
    print("a3 is greatest :", a3)

else:
    print("a4 is greatest :", a4)
    

p1 = "make a lot of money "
p2 = "buy a Iphone"
p3 = "subsribe now"