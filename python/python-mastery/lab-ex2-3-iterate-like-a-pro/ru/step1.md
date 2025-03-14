# Базовая итерация и распаковка последовательностей

В этом шаге мы рассмотрим базовую итерацию с использованием циклов `for` и распаковку последовательностей в Python. Итерация - это фундаментальный концепт в программировании, который позволяет последовательно проходить по каждому элементу в последовательности. Распаковка последовательностей, с другой стороны, позволяет удобно присваивать отдельные элементы последовательности переменным.

## Загрузка данных из CSV-файла

Начнем с загрузки некоторых данных из CSV-файла. CSV (Comma-Separated Values, значения, разделенные запятыми) - это распространенный формат файлов, используемый для хранения табличных данных. Чтобы начать, нам нужно открыть терминал в WebIDE и запустить интерпретатор Python. Это позволит нам интерактивно запускать код на Python.

```bash
cd ~/project
python3
```

Теперь, когда мы находимся в интерпретаторе Python, мы можем выполнить следующий код на Python для чтения данных из файла `portfolio.csv`. Сначала мы импортируем модуль `csv`, который предоставляет функциональность для работы с CSV-файлами. Затем мы открываем файл и создаем объект `csv.reader` для чтения данных. Мы используем функцию `next` для получения заголовков столбцов и преобразуем оставшиеся данные в список. Наконец, мы используем функцию `pprint` из модуля `pprint` для вывода строк в более читаемом формате.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

Вы должны увидеть вывод, похожий на следующий:

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Базовая итерация с использованием циклов `for`

Оператор `for` в Python используется для итерации по любой последовательности данных, такой как список, кортеж или строка. В нашем случае мы будем использовать его для итерации по строкам данных, которые мы загрузили из CSV-файла.

```python
for row in rows:
    print(row)
```

Этот код будет проходить по каждой строке в списке `rows` и выводить ее. Вы увидите каждую строку данных из нашего CSV-файла, выведенную по одной.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Распаковка последовательностей в циклах

Python позволяет распаковывать последовательности непосредственно в цикле `for`. Это очень полезно, когда вы знаете структуру каждого элемента в последовательности. В нашем случае каждая строка в списке `rows` содержит три элемента: имя, количество акций и цену. Мы можем распаковать эти элементы непосредственно в цикле `for`.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Этот код распакует каждую строку в переменные `name`, `shares` и `price`, а затем выведет их. Вы увидите данные, выведенные в более читаемом формате.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

Если вам не нужны некоторые значения, вы можете использовать `_` в качестве заполнителя, чтобы указать, что вы не заинтересованы в этих значениях. Например, если вы хотите вывести только имя и цену, вы можете использовать следующий код:

```python
for name, _, price in rows:
    print(name, price)
```

Этот код будет игнорировать второй элемент в каждой строке и выводить только имя и цену.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Расширенная распаковка с использованием оператора `*`

Для более продвинутой распаковки вы можете использовать оператор `*` в качестве подстановочного знака. Это позволяет собирать несколько элементов в список. Давайте сгруппируем наши данные по имени, используя эту технику.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

В этом коде мы сначала импортируем класс `defaultdict` из модуля `collections`. `defaultdict` - это словарь, который автоматически создает новое значение (в данном случае, пустой список), если ключ не существует. Затем мы используем оператор `*` для сбора всех элементов, кроме первого, в список с именем `data`. Мы сохраняем этот список в словаре `byname`, сгруппированном по имени. Наконец, мы выводим данные для IBM и проходим по ним, чтобы вывести количество акций и цену.

Вывод:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

В этом примере `*data` собирает все элементы, кроме первого, в список, который мы затем сохраняем в словаре, сгруппированном по имени. Это мощная техника для обработки данных с последовательностями переменной длины.
