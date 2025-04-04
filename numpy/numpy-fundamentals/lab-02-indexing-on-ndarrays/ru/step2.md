# Основное индексирование

Массивы NumPy можно индексировать с использованием стандартного синтаксиса Python `x[obj]`, где `x` - это массив, а `obj` - это выборка. Существует несколько типов индексирования, в зависимости от типа `obj`.

## Индексирование одного элемента

Индексирование одного элемента работает точно так же, как индексирование для других стандартных последовательностей Python. Нумерация начинается с 0, и допускаются отрицательные индексы для индексирования с конца массива.

```python
x = np.arange(10)
print(x[2])  # Вывод: 2
print(x[-2])  # Вывод: 8
```

## Многомерное индексирование

Массивы могут иметь несколько измерений, и индексирование работает одинаково для каждого измерения. Вы можете получить доступ к элементам в многомерном массиве, разделяя индекс каждого измерения запятой.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Вывод: 8
print(x[1, -1])  # Вывод: 9
```

## Индексирование подмассива

Если вы индексируете многомерный массив меньшим количеством индексов, чем измерений, вы получаете подмассив. Каждый указанный индекс выбирает массив, соответствующий оставшимся измерениям.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Вывод: [0, 1, 2, 3, 4]
```
