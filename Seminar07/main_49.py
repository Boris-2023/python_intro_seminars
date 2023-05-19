# Задача №49. 
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

import math

ell_sq = lambda rad: math.pi*rad[0]*rad[1]

def find_farthest_orbit (orbits: list) -> tuple:
    orbits_sq = [ell_sq(orbits[i]) for i in range(len(orbits))] #find the squares of orbits
    
    max_val = max_ind = -1 #initialization
    for i in range(len(orbits)):
        if max_val < orbits_sq[i] and orbits[i][0] != orbits[i][1]:
            max_val = orbits_sq[i]
            max_ind = i
    
    return orbits[max_ind]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(f"orbits:\t{orbits}\nthe farthest orbit:{find_farthest_orbit(orbits)}")


#--------> nice PYTHON
# import math

# ell_sq = lambda rad: math.pi*rad[0]*rad[1]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# orbits_sq = [ell_sq(orbits[i]) for i in range(len(orbits))] #find the squares of orbits
# res = orbits[ max([ (val, ind) for ind, val in enumerate(orbits_sq) if orbits[ind][0] != orbits[ind][1] ])[1] ]

# print(res)