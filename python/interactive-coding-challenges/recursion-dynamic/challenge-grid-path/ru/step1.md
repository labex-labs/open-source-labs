# Путь по сетке

## Задача

Дана прямоугольная сетка с валидными и невалидными ячейками. Реализуйте функцию для нахождения валидного пути для робота, чтобы он перемещался из верхнего левого угла в нижний правый угол. Если нет валидного пути, верните None. Если входные данные недействительны или матрица пуста, верните None.

## Требования

Требования к этому алгоритму следующие:

- Робот может двигаться только вправо и вниз.
- Некоторые ячейки могут быть недоступными.
- Сетка прямоугольная и не имеет зазубренности.
- Не всегда будет валидного пути для робота, чтобы добраться до нижнего правого угла.
- Входные данные не всегда будут действительными.
- Алгоритм должен соответствовать ограничениям по памяти.

## Пример использования

Рассмотрим следующую сетку:

```txt
o = валидная ячейка
x = невалидная ячейка

   0  1  2  3
0  o  o  o  o
1  o  x  o  o
2  o  o  x  o
3  x  o  o  o
4  o  o  x  o
5  o  o  o  x
6  o  x  o  x
7  o  x  o  o
```

- Обычный случай:

```txt
ожидалось = [(0, 0), (1, 0), (2, 0),
            (2, 1), (3, 1), (4, 1),
            (5, 1), (5, 2), (6, 2),
            (7, 2), (7, 3)]
```

- Нет валидного пути: В приведенном выше примере ячейка в строке 7, столбце 2 также невалидна -> None
- Входные данные None -> None
- Пустая матрица -> None
