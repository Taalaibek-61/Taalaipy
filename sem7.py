# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется
#  множество раз и вы не хотите ничего сломать): 
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно
# получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)
          
trasformation= lambda x: x 
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
    print(transformed_values)
    #my_nums = '182 34 56 786 89'

# my_list_0 = my_nums.split()
# print(my_list_0)

# my_list_1 = map(int, my_nums.split())
# print(my_list_1)
# print('Первый my_list_1')
# print(list(my_list_1))
# print('Второй my_list_1')
# print(list(my_list_1))

# my_list_1_2 = map(int, my_nums.split())
# print(next(my_list_1_2))
# print(next(my_list_1_2))
# print(next(my_list_1_2))
# print(next(my_list_1_2))
# print(next(my_list_1_2))
# print(next(my_list_1_2))
# print(next(my_list_1_2))

# my_filter = tuple(filter(lambda x: '8' in x, my_nums.split()))
# my_list_2 = list(map(int, my_filter))
# my_list_3 = list(map(int, my_filter))
# print(my_list_2)
# print(my_list_3)

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
#  орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
#    которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
#    Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные 
#    спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий 
#    длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары
#      чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей
#        эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс
#          в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий
#            такую  площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Вывод: 
# 2.5 10
# def find_farthest_orbit(list_of_orbits):
    #arr = list(filter(lambda x:x[0]!=x[1],list_of_orbits))
    #arr_2 = list(map(lambda x:x[0]*x[1],arr))
    #max_s = max(arr_2)
    #i_max = arr_2.index(max_s)
    #return(arr[i_max])
    # i_max = 0
    # s_max = 0
    #a,b,d,f = (12,34,'rfdg', 23)
    #for i,cur_tuple in enumerate(list_of_orbits):
    #    print(i, end=' индекс кортежа ')
    #    print(cur_tuple)
#     for i, el_tuple in enumerate(list_of_orbits):
#         s_cur = el_tuple[0] * el_tuple[1]
#         if el_tuple[0] != el_tuple[1] and s_max < s_cur:
#             i_max = i
#             s_max = s_cur
#     return list_of_orbits[i_max]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic 
# - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]				same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)
#        def same_by(characteristic, objects):
#     #for i in range(1,len(objects)):
#     #    if characteristic(objects[i]) != characteristic(objects[i -1]):
#     #        return False
#     #return True
#     #print(objects)
#     #map_obj = list(map(characteristic, objects))
#     #print(map_obj)
#     #print(set(map_obj))
#     #print(len(set(map_obj)))
#     print(len(set(map(characteristic, objects))) == 1)

#     return len(set(map(characteristic, objects))) == 1

# values = [1, 3, 11, 7]
# if same_by(lambda x: x % 2, values): # True - правда - да, False - ложь - нет
#     print('same')
# else:
#     print('different')