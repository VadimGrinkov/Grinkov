# Блок 1. Задача 2. Строки
randomString = input("введите строку - ")
print("Длина строки - ", len(randomString), "символа(ов)")
for i in randomString:
    if i == "c" or i == "C" or i == "с" or i == "С": # латиница и кириллица
        print("Символ <c> обнаружен")
print("Без 3-го символа-", randomString[0:2]+randomString[3:len(randomString)])
print("Без последнег)