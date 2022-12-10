import random

print("Welcome to Python world")
MinNum = int(input("Enter your min value: "))
MaxNum = int(input("Enter your max value: "))

num = random.randint(MinNum,MaxNum);
print("Range is (%d,%d) and randomly picked number is %d"%(minNum,maxNum,num))


if num > 0:
    print("{} is Positive number".format(num))
elif num == 0:
    print("{} is Zero".format(num))
else:
    print("{} is Negative number".format(num))

if (num % 2) == 0:
    print("{0} is Even number".format(num))
else:
    print("{0} is Odd number".format(num))

if num%num==0 and num%1==0:
    print('{0} is prime number'.format(num))
else:
    print('{0} is composite number'.format(num))
