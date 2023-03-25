'''
#Задача 2: Найдите сумму цифр трехзначного числа.

#Пример:*

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |

n=int (input("Введите трехзначное число: "))
sum = 0
if n > 99 and n < 1000:
    while n != 0:
        digit = n % 10
        sum += digit
        n = n // 10
    print(sum)
else:
    print('Ввели не трехзначное число')
           
#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
 #Вместе они сделали S журавликов. 
#Сколько журавликов сделал каждый ребенок, если известно,
#что Петя и Сережа сделали одинаковое количество журавликов, 
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
    
#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#    60 -> 10  40  10

S=int (input("Введите  число S: "))
a = S // 6
b = S // 6 * 4
print(f"Петя и Сереже сделали {a} журавликов, Катя сделала {b} журавликов")


#Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
#  вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. 
# билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость 
# билета.

#*Пример:


#385916 -> yes
#123456 -> no

num=int (input("Введите номер билета: "))
sum1 = 0
sum2 = 0
if num > 99999 and num <1000000:
    a = num // 1000
    d1 = a // 100
    d2 = a //10 % 10
    d3 = a % 10
    sum1 = d1 + d2 + d3
    b = num % 1000
    c1 = b // 100
    c2 = b //10 % 10
    c3 = b % 10
    sum2 = c1 + c2 + c3 
    if sum1 == sum2:
        print('Да билет счастливый')
    else:
        print('Нет билет несчастливый')

    


#Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по 
# прямой между дольками (то есть разломить шоколадку на два
#  прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no
n=int (input("Введите длину: "))
m=int (input("Введите ширину: "))
k=int (input("Введите количество долек: "))
if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')
'''


"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
2. Пользователь вводит число n. На следующих строках нужно вводить 1
 или 0, в ответе вывести количество наименее встречающихся из них
   (т.е либо количество 0 либо 1, в зависимости от того, кого меньше
"""
'''
from random import randint


n= int(input('Введите целое число от 1 до 10:'))
count1 = 0
count2 = 0
for _ in range(n):
    num = randint(0,1)
    print(num)
    if num == 0:
        count1 += 1
    elif num == 1:
        count2 += 1
print()
if count1 < count2:
   print(f'Наименьшее количество цифр 0: {count1}')
else:
   print(f'Наименьшее количество цифр 1: {count2}')
'''

"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""
'''
S = int(input("Введите сумму цифр S: "))
P = int(input("Введите произведение цифр P: "))
X = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
Y = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
if X + Y == S and X * Y == P:  
  print(X,Y)
else:
  print("Введены некорректные цифры")
  '''

"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
10 -> 1 2 4 8"""
'''
N = int(input('Введите цифру N:'))
S = 1
while(S * 2 < N):
    S = S * 2
print(S)
'''
'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число
X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках 
записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
'''
'''
from random import randint


N = int(input('Введите целое число от 1 до 10:'))
X = int(input('Введите целое число от 1 до 10:'))
count = 0
for _ in range(N):
    num = randint(0,10)
    print(num)
    if X == num:
        count += 1
print()
print(f"Указанное число встречается: {count} раз")
'''

'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
элемент к заданному числу X. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих 
строках записаны N целых чисел Ai. Последняя строка содержит число X


*Пример:*

5
    1 2 3 4 5
    6
    -> 5
    '''
'''
from random import randint
N = int(input('Введите размер массива целое число от 1 до 10:'))
#X = int(input('Введите целое число от 1 до 10:'))
array =[]
for _ in range(N):
    array. append(randint(0,10))
print(array)
X = int(input('Введите целое число от 1 до 10 для сравнения:'))
min = abs(X-array[0])
numMin = array[0]
for num in array[-1:]:
    min1 = abs(X - array[num])
    if min1 < min:
        min1 = min
        numMin = min
print(f"Наиболее близким числом к заданному числу является: {numMin}")
'''
'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет 
определенную ценность. В случае с английским алфавитом очки
распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы 
оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость
введенного пользователем слова. Будем считать, что на вход подается 
только одно слово, которое содержит либо только английские, 
либо только русские буквы.

*Пример:*

ноутбук
    12
    '''
'''
аrrayS = {'AEIOULNSTR': 1,'DG': 2,'BCMP': 3,'FHVWY': 4,
         'K': 5,'JX': 8,'QZ': 10,'АВЕИНОРСТ': 1,'ДКЛМПУ': 2,
          'БГЁЬЯ': 3,'ЙЫ': 4,'ЖЗХЦЧ': 5,'ШЭЮ': 8,'ФЩЪ': 10}

skr = input("Введите слово на английском или русском:").upper()
sum = 0
for a in skr:
    for key, value in arrayS.items():
        if a in key:
            sum += int(value)
            break
print(sum)
'''
'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть
 с повторениями). Выдать без повторений в порядке возрастания все те
числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого 
множества. m - кол-во элементов второго множества. Затем пользователь 
вводит сами элементы множеств.
'''
'''
from random import randint
n = int(input('Введите количество элементов первого множества:'))
m = int(input('Введите количество элементов второго множества:'))
arrayN = []
arrayM = []
for _ in range(n):
    arrayN.append(randint(0,10))
print(arrayN)
arrayN = set(arrayN)
print(arrayN)
for _ in range(m):
    arrayM.append(randint(0,10))
print(arrayM)
arrayM = set(arrayM)
print(arrayM)
arrayR = sorted(arrayN & arrayM)
print(arrayR)
'''

'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке
растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на 
них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора 
черники. Эта система состоит из управляющего модуля и нескольких 
собирающих модулей. Собирающий модуль за один заход, находясь
непосредственно перед некоторым кустом, собирает ягоды с этого куста и
с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль, находясь перед 
некоторым кустом заданной во входном файле грядки.
'''
from random import randint
size = randint(8, 10)
N = [randint(1, 10) for _ in range(size)]
print(N)

max_M = N[-1] + N[-2] + N[0]
sum = max_M

for i in range(0,size - 1):
   sum = N[i] + N[i-1] + N[i+1]
   if sum > max_M:
      max_M = sum
print(max_M)