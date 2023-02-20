# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
from random import randint
n = int(input("Введите число N элементов: "))
num_list_1= []
for i in range(n):
    num_list_1.append(randint(0, 10))
print(num_list_1)
m = int(input("Введите число M элементов: "))
num_list_2= []
for i in range(m):
    num_list_2.append(randint(0, 10))
print(num_list_2)
num_list_3 = sorted(num_list_1 + num_list_2)
checked_nums_list = []
for i in num_list_3:
    if num_list_3.count(i) > 1 and i not in checked_nums_list:
        checked_nums_list.append(i)
        print (i,end=' ')
