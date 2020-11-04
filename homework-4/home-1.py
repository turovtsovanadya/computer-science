import random

counter = 0
gun = [0, 0, 0, 1, 0, 0]

print("Вас приветствует игра Русская рулетка! Готовы крутить барабан? 1 - Крутить барабан, 0 - Выход")

lengthGun = len(gun)
num = int(input())

if num == 1:

    while counter < lengthGun:

        shot = random.choice(gun)
        counter += 1

        if shot == 1:
            print("Надо же! Вы пережили уже " + str(counter) + " попыток!")
            print("Вы проиграли!")
            indexShot = gun.index(shot)
            print("Индекс выстрела " + str(indexShot))
            break
        else:
            if counter == lengthGun:
                print("Надо же! Вы пережили уже " + str(counter) + " попыток!")
                print("Вы победили!")

else:
    print("Вы вышли из игры")
