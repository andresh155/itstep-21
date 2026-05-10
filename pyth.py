import math
def select_task():
    task = input("виберіть задавдання: 1-6 ")
    match task:
        case "1":
            task1()
        case "2":
            print("введіть 2 числа")
            n1 = int(input("перше число: "))
            n2 = int(input("друге число"))
            task2(n1, n2)
        case "3":
            s1 = input("введіть символ")
            n1 = int(input("введіть довжину"))
            b1 = input("введіть яка буде ось (x/y)")
            if b1 != "x" and b1 != "y":
                print("не вірно вказана дія")
                select_task()
            task3(s1, n1, b1)
        case "4":
            n1 = int(input("введіть перше число"))
            n2 = int(input("введіть друге число"))
            n3 = int(input("введіть третє число"))
            n4 = int(input("введіть четверте число"))
            print(task4(n1, n2, n3, n4))
        case "5":
            n1 = int(input("Введіть число"))
            print("является ли число простим: ")
            print(task5(n1))
        case "6":
            n1 = int(input("Введіть 6-значне число"))
            print("является ли число простим: ")
            print( task6(n1))
        case "exit":
            exit()
        case _:
            print("невірний вибір, спробуйте ще раз")
            select_task()
def task1():
    print('"Don\'t let the noise of others\' opinions drown out your own inner voice."')
    print("Steve Jobs")

def task2(n1, n2):
    for i in range (min(n1, n2), max(n1,n2)):
        if i % 2 == 0:
            continue
        print(i)
def task3(s1, n1, b1):
    if b1 == "x":
        print(s1*n1)
    else:
        for _ in range(1, n1):
            print(s1)
def task4(n1, n2, n3, n4):
    max_count = 0
    list = [n1, n2, n3, n4]
    for i in list:
        if i > max_count:
            max_count = i
    return max_count
def task5(n1):
    if n1 < 2:
        return False
    for i in range(2, n1//2+1):
        if n1 % i == 0:
            return False
    return True

def task6(n1):
    if n1[0] + n1[1] + n1[2] == n1[3] + n1[4] + n1[5]:
        return True
    return False

while True:
    select_task()