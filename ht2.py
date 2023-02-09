# В фермерском хозяйстве.....
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

bush_quantity = int(input('Введите кол - во кустов: '))
list = list()
print('Введите количество ягод на каждом кусте: ')
for i in range (bush_quantity):
    num = int(input())
    list.append(num)

list_1 = []
for i in range(len(list) - 1):
    list_1.append(list[i-1] + list[i] + list[i+1])
list_1.append(list[-2] + list[-1] + list[0])

print('Максимальное возможное кол - во собранных ягод:')
print(max(list_1))    


