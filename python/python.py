# print ('Hello, World!')
# print ('Bye, World!')
# print (5)
# print (10)
# print (5+10)
# print (3*7, (17-2)*8)
# print (2**16)
"""
print (37 / 3)
print (37 // 3)
print (37 % 3)
"""
# print ("Как Вас зовут?")
# userName = input()
# userName = "Привет, " + userName + "!"
# print (userName)
"""
print ("Как Вас зовут?")
userName = input()
print ("Привет, " +userName+ "!")
"""
"""
a = int(input())
b = int(input())
s = a + b
print (s)
"""
"""
apples = 10
print(apples == 10)
print(apples < 10)
print(apples <= 10)
print(apples > 10)
print(apples >= 10)
print(apples != 10)
"""
"""
apples = 10
print(apples < 20 and apples > 5)
print(apples < 10 and apples > 5)
print(apples <= 10 and apples > 5)
print(apples < 3 or apples > 7)
print(apples < 3 or apples > 15)
print(apples < 3 or apples > 10)
"""
"""
apples = 10
print(not (apples < 3))
print(not apples < 3)
print(not (apples < 20 or apples > 5))
print(not apples < 20 or apples > 5)
"""
"""
day = int(input())
month = int(input())
print(day == 28 and month == 7)
print(not (day == 28 and month == 7))
"""
"""
a = int(input())
if a > 0:
    print('Положительное')
else:
    print('Неположительное')

b = int(input())
if b <= 0:
    print('меньше либо равно 0')
"""
"""
num = int(input())
if num % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
"""
"""
a = int(input())
if a != 0:
    if a > 0:
        print('Положительное')
    else:
        print('Неположительное')
else:
    print('Равно 0')
"""
"""
a = int(input())
if a > 0:
    if a % 2 == 0:
        print('Четное положительное')
    else:
        print('Нечетное положительное')
elif a < 0:
    if a % 2 == 0:
        print('Четное отрицательное')
    else:
        print('Нечетное отрицательное')
else:
    print('Равно 0')
"""
"""
dog = 'Гав, гав!'
print(len (dog) < 5)
print(len(dog) > 10 or len(dog) == 10)
print(len(dog))
print(len(dog)**2 + 100)
"""
"""
number = int(input())
counter = 0
sum = 0
for i in range (0, 10000):
    if counter < 10:
        sum = sum + number
        counter += 1
    else:
        break
print(sum)
"""
"""
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
"""
"""
numbers = [1, 2, 3, 4, 5]
print(numbers[-3])
print(numbers[-2])
print(numbers[-1])
print(numbers[-0])
"""
"""

numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers[0] = 'yes'
numbers[2] = 'no'
numbers[3] = [1,2,3]
print(numbers)

numbers[3][0] = 'it'
numbers[3][1] = 'yes'
numbers[3][2] = 10
print(numbers)
print(numbers[3][2])
print(numbers[3])
print(len(numbers))
print(len(numbers[3]))
print(len(numbers[3][2]))
"""
"""
list1 = [1, 2]
list2 = list1
list1.append(5)
print(list1)
print(list2)
import copy
list3 = copy.deepcopy(list1)
list3.append(7)
print(list1)
print(list3)
"""
sent = "What a wonderful world!"

words = sent.split()
print(words)