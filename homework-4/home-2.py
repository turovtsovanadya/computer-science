#"Подземелье", "Коридор", "Оружейная", "Спальня", "Холл", "Кухня", "Балкон"
#1 - север, 2 - восток, 3 - юг, 4 - запад

roomList = []
room = ["Подземелье", 3, 1, None, None]
roomList.append(room)
room = ["Коридор", 4, 2, None, 0]
roomList.append(room)
room = ["Оружейная", 5, None, None, 1]
roomList.append(room)
room = ["Спальня", 6, 4, 0, None]
roomList.append(room)
room = ["Холл", 6, 5, 1, 3]
roomList.append(room)
room = ["Кухня", 6, None, 2, 4]
roomList.append(room)
room = ["Балкон", None, None, None, None]
roomList.append(room)

currentRoomIndex = 0

directionList = ["Север", "Восток", "Юг", "Запад"]

# currentRoomName = roomList[0][0]
# lastRoom = roomList[6][0]

while currentRoomIndex != 6:
    print("-----------")

    currentRoom = roomList[currentRoomIndex]
    direction = ""

    for i in range(1, 5):
        if currentRoom[i] != None:
            direction += directionList[i-1] + " "

    print(direction)
    print("Введите направление")

    userDirection = input()

    if not (userDirection in directionList):
        print("Введите другое направление")
        continue


    if userDirection == directionList[0]:
        nextRoom = currentRoom[1]
        if nextRoom == None:
            print("Введите другое направление")
            continue
        else:
            currentRoomIndex = nextRoom

    if userDirection == directionList[1]:
        nextRoom = currentRoom[2]
        if nextRoom == None:
            print("Введите другое направление")
            continue
        else:
            currentRoomIndex = nextRoom

    if userDirection == directionList[2]:
        nextRoom = currentRoom[3]
        if nextRoom == None:
            print("Введите другое направление")
            continue
        else:
            currentRoomIndex = nextRoom

    if userDirection == directionList[3]:
        nextRoom = currentRoom[4]
        if nextRoom == None:
            print("Введите другое направление")
            continue
        else:
            currentRoomIndex = nextRoom

print("Congratulation")


