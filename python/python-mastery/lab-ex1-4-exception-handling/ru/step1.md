# Определение функции

На этом этапе мы научимся создавать функции. Функция в Python представляет собой блок организованного, переиспользуемого кода, который используется для выполнения одной связанной операции. Здесь наша функция будет считывать данные о портфеле из файла и вычислять общую стоимость. Это полезно, так как после создания этой функции мы можем использовать ее несколько раз с разными файлами портфелей, избавляясь от необходимости повторно писать один и тот же код.

## Понимание проблемы

В предыдущем практическом занятии (лабораторной работе) вы, возможно, написали код для считывания данных о портфеле и вычисления общей стоимости. Однако этот код, вероятно, был написан таким образом, что его нельзя легко переиспользовать. Теперь мы преобразуем этот код в переиспользуемую функцию.

Файлы с данными о портфеле имеют определенный формат. Они содержат информацию в виде "Символ Количество_акций Цена". Каждая строка в файле представляет собой позицию в портфеле акций. Например, в файле с именем `portfolio.dat` вы можете увидеть строки следующего вида:

```
AA 100 32.20
IBM 50 91.10
...
```

Здесь первая часть (например, "AA" или "IBM") - это символ акции, который является уникальным идентификатором акции. Вторая часть - это количество акций, которые вы владеете, а третья часть - это цена за одну акцию.

## Создание функции

Создадим файл Python с именем `pcost.py` в директории `/home/labex/project`. Этот файл будет содержать нашу функцию. Вот код, который мы поместим в файл `pcost.py`:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extract the data (symbol, shares, price)
            shares = int(fields[1])
            price = float(fields[2])
            # Add the cost to our running total
            total_cost += shares * price

    return total_cost

# Call the function with the portfolio.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

В этом коде мы сначала определяем функцию с именем `portfolio_cost`, которая принимает `filename` в качестве аргумента. Внутри функции мы инициализируем переменную `total_cost` со значением 0.0. Затем мы открываем файл с помощью функции `open` в режиме чтения (`'r'`). Мы используем цикл `for` для прохода по каждой строке в файле. Для каждой строки мы разбиваем ее на поля с помощью метода `split()`. Затем мы извлекаем количество акций и преобразуем его в целое число, а цену - в число с плавающей точкой. Мы вычисляем стоимость данной позиции в портфеле, умножив количество акций на цену, и добавляем ее к `total_cost`. Наконец, мы возвращаем `total_cost`.

Часть `if __name__ == '__main__':` используется для вызова функции, когда скрипт запускается напрямую. Мы передаем путь к файлу `portfolio.dat` в функцию и выводим результат.

## Тестирование функции

Теперь запустим программу, чтобы проверить, работает ли она. Мы должны перейти в директорию, где находится файл `pcost.py`, и затем запустить скрипт Python. Вот команды для этого:

```bash
cd /home/labex/project
python3 pcost.py
```

После выполнения этих команд вы должны увидеть следующий вывод:

```
44671.15
```

Этот вывод представляет общую стоимость всех акций в портфеле.

## Понимание кода

Разберем пошагово, что делает наша функция:

1. Она принимает `filename` в качестве входного параметра. Это позволяет нам использовать функцию с разными файлами портфелей.
2. Она открывает файл и читает его построчно. Это делается с помощью функции `open` и цикла `for`.
3. Для каждой строки она разбивает строку на поля с помощью метода `split()`. Этот метод разбивает строку на список строк на основе пробелов.
4. Она преобразует количество акций в целое число и цену в число с плавающей точкой. Это необходимо, так как данные, считанные из файла, имеют строковый формат, и мы должны выполнять арифметические операции с ними.
5. Она вычисляет стоимость (количество_акций \* цена) для каждой позиции в портфеле и добавляет ее к текущей общей стоимости. Это дает нам общую стоимость портфеля.
6. Она возвращает окончательную общую стоимость. Это позволяет нам использовать результат в других частях нашей программы, если это необходимо.

Эта функция теперь может быть переиспользована. Мы можем вызывать ее с разными файлами портфелей, чтобы вычислить их стоимость, что делает наш код более эффективным и легким в поддержке.
