def binary_search(list, number, start, stop):
    if start > stop:
        return -1

    else:

        mid = (start + stop) // 2

        if number > list[mid]:
            return binary_search(list, number, mid + 1, stop)
        elif number < list[mid]:
            return binary_search(list, number, start, mid - 1)
        else:
            return mid


list = [0, 0 , 0 , 1, 3, 4, 5, 6, 8, 9, 12, 14, 26, 36, 46, 58]
start = 0
stop = len(list)-1

number = int(input("Введи число"))

x = binary_search(list, number, start, stop)

if x==-1:
    print('Числа в списке нет')
else:
    print(f"Число  {number} найдено по индексом  {x}")

