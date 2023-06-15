#1.WAP to find greatestNo
def greatestNo(a,b,c):
    if a>b and a>c:
        message =a
    elif b>a and b>c:
        message =b
    else:
        message=c
    return message

#2. WAP To check even_odd
def even_odd(num):
    if num%2==0:
        message='even'
    else:
        message='odd'
    return message

#3. WAP to check leap_year
def leap_year(year):
    if year%100==0 and year%400==0:
        message='leap Year'
    elif year%4==0 and year%100!=0:
        message='leap Year'
    else:
        message="Not Leap Year"
    return message

#4 WAP to use range function
def rangeFun():
    for i in range(10):
        print(i)
# rangeFun()

#5. WAP to find sum of natural
def sumofnatural(num):
    sum=0
    for i in range(1,num+1,1):
        sum=sum+i
    return sum
# print(sumofnatural(10))

#6. WAP to find factorial 
def factorial(num):
    result=1
    for i in range(num,0,-1):
        result=result*i
    return result
# print(factorial(5))

#7. WAP to reverse the given number
def reverse(num):
    while num>0:
        result=0
        rem=num%10
        result=result*10+rem
        num=num//10
        print(result,end="")
# reverse(12345)

# 8. WAP to check palindrome number
def palindrome(n=1221):
    temp=1221
    result=0
    while n>0:
        rem=n%10
        result=result*10+rem
        n=n//10
    if(result==temp):
        print("palindrome Numbers")
    else:

      print("not a palindrome")

# 9. WAP to digitCount
def digitCount(n=14532):
    count=0
    while n>0:
        rem=n%10
        count=count+1
        n=n//10
    return count
# digitCount()
#10. WAp to find table of any number
def table(num):
    for i in range(1,11,1):
        result=num*i
        # print(result)
      
# 11.  Armstrong Number Program 153,1,1634 => 1^3+5^3+3^3=1+125+27=153

def armstrong(num=1634):
    count=0
    temp=num
    arm=num
    result=0
    while num>0:
        rem=num%10
        count=count+1
        num=num//10
    while temp>0:
        rem=temp%10
        result=result+pow(rem,count)
        temp=temp//10
    if arm==result:
        print("Yes ! armstrong")
    else:
        print("No ! armstrong")
# armstrong() 
