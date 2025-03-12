# Чтение портфеля из CSV-файла

На этом этапе мы создадим функцию, которая читает данные о акциях из CSV-файла и возвращает список объектов `Stock`. Объект `Stock` представляет собой пакет акций, и по завершении этого этапа вы сможете прочитать портфель акций из CSV-файла.

## Понимание CSV-файлов

CSV (Comma-Separated Values, разделенные запятыми значения) - это очень распространенный формат для хранения табличных данных. Представьте его как простую электронную таблицу. Каждая строка в CSV-файле представляет собой строку данных, а столбцы в этой строке разделены запятыми. Обычно первая строка CSV-файла содержит заголовки. Эти заголовки описывают, какого рода данные находятся в каждом столбце. Например, в CSV-файле с портфелем акций заголовками могут быть "Name", "Shares" и "Price".

## Инструкции по реализации

1. Сначала откройте файл `stock.py` в вашем редакторе кода. Если он уже открыт, это замечательно! Если нет, найдите его и откройте. Именно здесь мы будем добавлять нашу новую функцию.

2. После того, как файл `stock.py` открыт, найдите комментарий `# TODO: Add read_portfolio(filename) function here`. Этот комментарий является меткой, которая показывает, где нужно разместить нашу новую функцию.

3. Ниже этого комментария добавьте следующую функцию. Эта функция называется `read_portfolio`, и она принимает имя файла в качестве аргумента. Цель этой функции - прочитать CSV-файл, извлечь данные о акциях и создать список объектов `Stock`.

```python
def read_portfolio(filename):
    """
    Read a CSV file containing portfolio data and return a list of Stock objects.

    Args:
        filename (str): Path to the CSV file

    Returns:
        list: A list of Stock objects
    """
    portfolio = []

    with open(filename, 'r') as f:
        headers = next(f).strip().split(',')  # Skip the header line

        for line in f:
            row = line.strip().split(',')
            name = row[0]
            shares = int(row[1])
            price = float(row[2])

            # Create a Stock object and add it to the portfolio list
            stock = Stock(name, shares, price)
            portfolio.append(stock)

    return portfolio
```

Разберем, что делает эта функция. Сначала она создает пустой список с именем `portfolio`. Затем она открывает CSV-файл в режиме чтения. Инструкция `next(f)` пропускает первую строку, которая является строкой заголовка. После этого она проходит по каждой строке в файле. Для каждой строки она разбивает строку на список значений, извлекает имя, количество акций и цену, создает объект `Stock` и добавляет его в список `portfolio`. Наконец, она возвращает список `portfolio`.

4. После добавления функции сохраните файл `stock.py`. Вы можете сделать это, нажав `Ctrl+S` на клавиатуре или выбрав "File > Save" в меню редактора кода. Сохранение файла гарантирует, что ваши изменения будут сохранены.

5. Теперь нам нужно протестировать нашу функцию `read_portfolio`. Создайте новый Python-скрипт с именем `test_portfolio.py`. Этот скрипт импортирует функцию `read_portfolio` из файла `stock.py`, читает портфель из CSV-файла и выводит информацию о каждой акции в портфеле.

```python
# test_portfolio.py
from stock import read_portfolio

# Read the portfolio from the CSV file
portfolio = read_portfolio('portfolio.csv')

# Print information about each stock
for stock in portfolio:
    print(f"Name: {stock.name}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

# Print the total number of stocks in the portfolio
print(f"\nTotal number of stocks in portfolio: {len(portfolio)}")
```

В этом скрипте мы сначала импортируем функцию `read_portfolio`. Затем мы вызываем функцию с именем файла `portfolio.csv`, чтобы получить список объектов `Stock`. После этого мы проходим по списку и выводим информацию о каждой акции. Наконец, мы выводим общее количество акций в портфеле.

6. Чтобы запустить тестовый скрипт, откройте терминал или командную строку, перейдите в директорию, где находится файл `test_portfolio.py`, и выполните следующую команду:

```bash
python3 test_portfolio.py
```

Если все работает правильно, вы должны увидеть вывод, в котором перечислены все акции из файла `portfolio.csv`, а также их имена, количество и цены. Вы также должны увидеть общее количество акций в портфеле.

```
Name: AA, Shares: 100, Price: $32.20
Name: IBM, Shares: 50, Price: $91.10
Name: CAT, Shares: 150, Price: $83.44
Name: MSFT, Shares: 200, Price: $51.23
Name: GE, Shares: 95, Price: $40.37
Name: MSFT, Shares: 50, Price: $65.10
Name: IBM, Shares: 100, Price: $70.44

Total number of stocks in portfolio: 7
```

Этот вывод подтверждает, что ваша функция `read_portfolio` правильно читает CSV-файл и создает объекты `Stock` на основе его данных.
