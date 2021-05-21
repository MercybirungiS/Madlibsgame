# print("Hello World")
# a="hello akirachichix"
# print("hello\vakirachix")
# fruits=("mango.prineapple")
# # x=(.)

# # print(x[1])
# x=[2,9,16,20]
# m=1
# for a in x:
#     print(m*a)
# def multiplyList(myList) :
     
#     # Multiply elements one by one
#     result = 1
#     for x in myList:
#          result = result * x
#     return result
     
# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))

# num1=input("Enter a number:")
# num2=input("Enter another number:")
# results=float(num1)+int(num2)
# print(results)

# # madlibs game 
# color =input("Enter a color:")
# plural_noun=input("Enter a plural noun:")
# celebrity=input("Enter a celebrity:")

# print ("Roses are " + color)
# print(plural_noun+ "are blue ")
# print("I love "+celebrity)

# friends =["Mercy ","Faith","Hesed"]
# print(friends[1:3])
# friends[0]="Susan"
# print(friends[0:])
# friends.clear()
# print(friends)
# # list functions
# numbers=[2,8,10,12,14,18,14,10]
# nums2=[9,10,17]
# numbers.extend(nums2)
# print(numbers)
# numbers.insert(1,"9")
# print(numbers)
# numbers.remove(17)
# print(numbers)
# print(numbers.index(18))
# print(numbers.count(10))
# x=[2,4,5,7,19,34]
# x.sort()
# print(x)
# x.reverse()
# print(x)
# x2=[2,8,19,20,85]
# x2.extend(x)
# print(x2)
# print(sum(x2))
# print(max(x2))
# print(min(x2))
# coordinates=[(4,5,8),(2,8),(7,8)]
# coordinates[1]=10
# print(coordinates)

 

# def cube (num):
#    return  num*num*num

# result=cube(4)
# print(result)

# is_male=False

# if is_male:
#     print("You are a male")
# else:
#     print("you are female")

# dict={"name":"Mercy","age":16,"city":"Kampala"}
# print(dict)
# print(dict["name"])
# dict["color"]="brown"
# print(dict)
# dict["city"]="Nairobi"
# print(dict)
# print("name" in dict)
# keys=dict.keys()
# print(keys)
# values=dict.values()
# print(values)

 
# mercy={"name":"Mercy","age":24,"country":"Uganda"}
# carol={"name":"Carol","age":24,"country":"Uganda"}
# faith={"name":"Faith","age":24,"country":"Uganda"}
# aisha={"name":"Aisha","age":24,"country":"Uganda"}
# students=[mercy,carol,faith,aisha]
# print(students)

# for student in students:
#     name=student["name"]
#     age=student["age"]
#     country=student["country"]
#     sentence=(f"{name} is {age} years old and is from {country}")
#     print(sentence)


# x={'a':1,'b':2,'c':3}
# sum=0
# values=x.values()
# for m in values:
#     sum=sum+m
#     print(sum)

# x=range(10)
# print(x)
# for y in x:
#     print(y)
#     a=range(2,10)
#     for x in a:
#         print(x)
#         x=range(10)
#         for y in x:
#             if y%3==0:
#                 print(y)
#             else:
#                 print("uuu")
# i=range(10)
# for n in i:
#     if n%3!=0:
#         print(n)
# u=range(30)
# for n in u:
#     if n%5==0:
#         print(n)
#     elif n%7==0:
#         print(n)
#     else:
#         print("Fizz")
        



# write a function that accepts an integer and returs the factorial of that number ,use the range 
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

factorial(9)





