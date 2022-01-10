from datetime import datetime
import time

def prefix(x):
    p = [0]*len(x)
    j = 0
    i = 1
    while i < len(x):
        if x[j] != x[i]:
            if j > 0:
                j = p[j-1]
            else:           
                i += 1
        else:               
            p[i] = j + 1
            i += 1
            j += 1  
    return p

def kmpSearch(sub, x):
    k = 0
    l = 0
    p = prefix(sub)
    while k < len(x):
        if sub[l] == x[k]:
            k += 1
            l += 1
            if l == len(sub):
                return k - len(sub)
        elif l > 0:
            l = p[l-1]
        else:
            k += 1
    return -1

i = 1
x = input("Введите строку - ")
#sub = input("Введите подстроку - ")
while i == 1:
    enter_info = input("Введите желаемую операцию:\nF - найти подстроку\nI - ввести подстроку\nC - сменить строку\nZ - выход\n")
    if enter_info == "i" or enter_info == "I":
        sub = input("Введите подстроку - ")
        print("Текущая подстрока - " + sub)
    elif enter_info == "F" or enter_info == "f":
        start_time_default = datetime.now()
        search = sub in x
        if search:
            end_time_default = datetime.now()
            start_time_KMP = datetime.now()
            kmpSearch(x, sub)
            end_time_KMP = datetime.now()
            print("Подстрока найдена")
            print("Время поиска через встроенную функцию - ", end_time_default - start_time_default)
            print("Время поиска через алгоритм КМП - ", end_time_KMP - start_time_KMP)
        else:
            print("Подстрока не найдена")
    elif enter_info == "c" or enter_info == "C":
        x = input("Введите новую строку - ")
    elif enter_info == "z" or enter_info == "Z":
        quit()



input("Нажмите для продолжения...")

