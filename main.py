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
    ('Ввели не трехзначное число')
           
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



"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
10 -> 1 2 4 8"""