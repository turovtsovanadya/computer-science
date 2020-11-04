print("Компьютер загадал некоторое число от 1 до 100. Попробуйте угадать его!")

import random
number = random.randint(1, 100)

print("Какое число от 1 до 100 я загадал?")

counter = 0
numInput = int(input())

while number != numInput:
    if number < numInput:
        print("Число меньше")
    else:
        print("Число больше")
    counter += 1
    numInput = int(input())

print("Вы угадали. Количество попыток составило " + str(counter + 1))



