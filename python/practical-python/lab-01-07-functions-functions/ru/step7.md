# Упражнение 1.30: Преобразование скрипта в функцию

Возьмите код, который вы написали для программы `pcost.py` в упражнении 1.27, и преобразуйте его в функцию `portfolio_cost(filename)`. Эта функция принимает имя файла в качестве входных данных, читает данные портфеля из этого файла и возвращает общую стоимость портфеля в виде числа с плавающей точкой.

Для использования вашей функции измените вашу программу так, чтобы она выглядела примерно так:

```python
# pcost.py
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = f.readlines()
        headers = rows[0].strip().split(",")
        for row in rows[1:]:
            row_data = row.strip().split(",")
            nshares = int(row_data[1])
            price = float(row_data[2])
            total_cost += nshares * price

    return total_cost


import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a filename:")

cost = portfolio_cost(filename)
print("Total cost:", cost)
```

При запуске вашей программы вы должны увидеть такой же вывод, как и раньше. После запуска программы вы также можете вызвать вашу функцию интерактивно, набрав это:

```bash
$ python3 -i pcost.py
```

Это позволит вам вызывать вашу функцию из интерактивного режима.

```python
>>> portfolio_cost('portfolio.csv')
44671.15
>>>
```

Возможность экспериментировать с вашим кодом интерактивно полезна для тестирования и отладки.
