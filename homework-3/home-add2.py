print("Компьютер загадал некоторое число от 0 до 100. Попробуйте угадать его!")

import random
number = random.randint(0, 100)

print("Какое число от 0 до 100 я загадал?")

counter = 0
numInput = -1
availableSymbols = "0123456789"
warningString = "Русским же языком попросили ввести ИМЕННО число oт 0 до 100..."

while number != numInput:
    counter += 1

    numInput = input()
    numInputLen = len(numInput)

    if numInputLen == 0:
        print(warningString)
        continue
    if numInputLen == 1:
        if not(numInput[0] in availableSymbols):
            print(warningString)
            continue
    elif numInputLen == 2:
        if not(numInput[0] in availableSymbols) or not(numInput[1] in availableSymbols):
            print(warningString)
            continue
    elif numInputLen >= 3:
        if numInput != "100":
            print(warningString)
            continue

    numInputInt = int(numInput)

    if number == numInputInt:
        break

    elif number < numInputInt:
        print("Число меньше")
    else:
        print("Число больше")

print("Вы угадали. Количество попыток составило " + str(counter))