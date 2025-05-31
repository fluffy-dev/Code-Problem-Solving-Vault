"""
link: https://coderun.yandex.ru/selections/2024-summer-backend/problems/biggest-square

26. Наибольший квадрат

Вам дано описание дачного участка, который представляет собой клетчатый прямоугольник n × m n×m. В части клеток находятся ямы. Требуется найти на участке квадрат с наибольшей стороной, в котором нет ям.

Гарантируется, что есть хотя бы одна клетка без ямы.
Формат ввода

Вводятся два целых числа n n и m ( 1 ≤ n , m ≤ 1000 ) m(1≤n,m≤1000) — ширина и высота участка.

В следующих n n строках вводится по m m чисел a i , j ai,j​ ( 1 ≤ i ≤ n , 1 ≤ j ≤ m , a i , j ∈ { 0 , 1 } 1≤i≤n,1≤j≤m,ai,j​∈{0,1}) — описание участка. Значение 0 соответствует яме, а 1 1 — нормальной высоте клетки.
Формат вывода

Требуется вывести три числа — длину стороны оптимального квадрата и координаты его левого верхнего угла.
Ограничения

Ограничение времени

    2 с

Ограничение памяти

    512 МБ

Пример 1
Ввод

1 1
1

Вывод

1
1 1

Пример 2
Ввод

3 5
1 1 0 0 0
1 1 1 1 1
0 0 0 1 1

Вывод

2
2 4


"""


import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_side_len = 0
    ans_r, ans_c = 0, 0

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if grid[r - 1][c - 1] == 1:
                current_val_in_dp = 1 + min(dp[r - 1][c],
                                            dp[r][c - 1],
                                            dp[r - 1][c - 1])
                dp[r][c] = current_val_in_dp

                current_top_left_r = r - current_val_in_dp + 1
                current_top_left_c = c - current_val_in_dp + 1

                if current_val_in_dp > max_side_len:
                    max_side_len = current_val_in_dp
                    ans_r = current_top_left_r
                    ans_c = current_top_left_c
                elif current_val_in_dp == max_side_len and max_side_len > 0:
                    if current_top_left_r > ans_r:
                        ans_r = current_top_left_r
                        ans_c = current_top_left_c
                    elif current_top_left_r == ans_r and current_top_left_c > ans_c:
                        ans_c = current_top_left_c
    print(max_side_len)
    print(ans_r, ans_c)




if __name__ == '__main__':
    main()
