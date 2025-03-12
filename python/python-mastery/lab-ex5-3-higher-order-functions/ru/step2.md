# Создание функции высшего порядка

В Python функция высшего порядка - это функция, которая может принимать другую функцию в качестве аргумента. Это позволяет добиться большей гибкости и повторного использования кода. Теперь давайте создадим функцию высшего порядка с именем `convert_csv()`. Эта функция будет обрабатывать общие операции по обработке данных в формате CSV, при этом позволяя вам настраивать, как каждая строка CSV преобразуется в запись.

Откройте файл `reader.py` в WebIDE. Мы собираемся добавить функцию, которая будет принимать итерируемый объект с данными в формате CSV, функцию преобразования и, по желанию, заголовки столбцов. Функция преобразования будет использоваться для преобразования каждой строки CSV в запись.

Вот код функции `convert_csv()`. Скопируйте и вставьте его в файл `reader.py`:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Давайте разберем, что делает эта функция. Сначала она инициализирует пустой список с именем `records` для хранения преобразованных записей. Затем она использует функцию `csv.reader()` для чтения строк данных в формате CSV. Если заголовки не предоставлены, она берет первую строку в качестве заголовков. Для каждой последующей строки она применяет `conversion_func` для преобразования строки в запись и добавляет ее в список `records`. Наконец, она возвращает список записей.

Теперь нам нужна простая функция преобразования для тестирования нашей функции `convert_csv()`. Эта функция будет принимать заголовки и строку и преобразовывать строку в словарь, используя заголовки в качестве ключей.

Вот код функции `make_dict()`. Добавьте эту функцию также в файл `reader.py`:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

Функция `make_dict()` использует функцию `zip()` для сопоставления каждого заголовка с соответствующим значением в строке, а затем создает словарь из этих пар.

Давайте протестируем эти функции. Откройте оболочку Python, выполнив следующие команды в терминале:

```bash
cd ~/project
python3 -i reader.py
```

Опция `-i` в команде `python3` запускает интерпретатор Python в интерактивном режиме и импортирует файл `reader.py`, так что мы можем использовать только что определенные функции.

В оболочке Python выполните следующий код для тестирования наших функций:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

Этот код открывает файл `portfolio.csv`, использует функцию `convert_csv()` с функцией преобразования `make_dict()` для преобразования данных CSV в список словарей, а затем выводит результат.

Вы должны увидеть вывод, похожий на следующий:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

Этот вывод показывает, что наша функция высшего порядка `convert_csv()` работает правильно. Мы успешно создали функцию, которая принимает другую функцию в качестве аргумента, что позволяет нам легко изменять способ преобразования данных CSV.

Чтобы выйти из оболочки Python, вы можете ввести `exit()` или нажать Ctrl+D.
