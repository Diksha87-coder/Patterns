# EVEN ODD
#a=int(input("enter the number : \n"))
#if a%2==0:
#   print("even")
#else:
#    print("odd")

# SUM OF TWO NUMBERS
#a=int(input("enter the first number \n"))
#b=int(input("enter the second number \n"))
#print("sum =",a+b)


#GREATEST OF THRREE NUMBERS
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a >= b and a >= c:
#     print("Greatest number is:", a)
# elif b >= a and b >= c:
#     print("Greatest number is:", b)
# else:
#     print("Greatest number is:", c)

    
    
#PALLINDRONE 
# num=int(input("enter the number \n"))
# temp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if temp == rev:
#     print("pallindrome")
# else:
#     print("not palindrome")

# ARMSTRONG
# num=int(input("enter the number \n"))
# temp=num
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+(digit**3)
#     num=num//10
# if temp == num:
#     print("Armstrong")
# else:
#     print("not Armstrong")

#PRIME
# n=int(input("enter te number :"))
# flag=1

# for i in range (2,(n//2)+1):
#      if(n%i == 0):
#             flag +=1
#             break ;
# if (flag==1):
#     print("prime")
# else:
#     print("not prime")

#LEAP YEAR
# y=int(input("enter the year:"))
# if(y%400==0) or(y%4==0) and(y%100!=0):
#   print("leap year")
# else:
#  print("not leap year")

#POSITIVE OR NEGATIVEL
# n=int(input())
# if n1>0:
#     print("n is positive")
# else:
#     print("n is negative")

# DIVISIBLE BY 3 AND 5
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i,end " ")

# PRODUCT OF DIGIT OF GIVEN NUMBER
# num = int(input("Enter a number: "))
# product = 1
# while num > 0:
#     digit = num % 10        
#     product = product*digit         
#     num //= 10               
# print("Product of digits =", product)

# SUM OF EVEN AND PRODUCT OF ODD DIGITS
# num = int(input("Enter a number: "))
# sum_even = 0
# product_odd = 1
# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:      
#         sum_even += digit
#     else:                    
#         product_odd *= digit
#     num //= 10
# print("Sum of even digits =", sum_even)
# print("Product of odd digits =", product_odd)


# COUNT TOTAL NUMBER OF FACTOR OF A GIVEN NUMBER
# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:   # agar i num ka factor hai
#         count =count+1
# print("Total number of factors =", count)

#FACTORIAL OF A GIVEN NUMBER
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact =fact*i
# print("Factorial =", fact)


#FABONACCI SERIES 
#num = int(input("Enter how many terms: "))
# a = 0   
# b=1
# print(a, b, end=" ")
# for i in range(2, num):
#     c = a + b
#     print(c, end=" ")
#     a=b
#     b=c


# REVERSE OF A GIVEN NUMBER
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10        
#     rev = rev * 10 + digit  
#     num //= 10              
# print("Reversed number =", rev)

# AREA OF RECTANGLE 
# def rectanglearea(width, height):
#     area = width * height
#     return area
# w = float(input("Enter width: "))
# h = float(input("Enter height: "))
# print("Area of rectangle =", rectanglearea(w, h))

