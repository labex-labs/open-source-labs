# Упражнение 4.6: Использование наследования для получения различных выводов

Класс `TableFormatter`, который вы определили в части (a), предназначен для расширения с использованием наследования. На самом деле, это и есть вся идея. Чтобы проиллюстрировать, определите класс `TextTableFormatter` так:

```python
# tableformat.py
...
class TextTableFormatter(TableFormatter):
    '''
    Выводит таблицу в формате простого текста
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 +' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
```

Измените функцию `portfolio_report()` так и попробуйте ее:

```python
# report.py
...
def portfolio_report(portfoliofile, pricefile):
    '''
    Создает отчет о портфеле по данным файлов портфеля и цен.
    '''
    # Читаем данные из файлов
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Создаем данные для отчета
    report = make_report_data(portfolio, prices)

    # Выводим их
    formatter = tableformat.TextTableFormatter()
    print_report(report, formatter)
```

Это должно произвести такой же вывод, как и раньше:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Однако, давайте изменим вывод на что-то другое. Определите новый класс `CSVTableFormatter`, который выводит данные в формате CSV:

```python
# tableformat.py
...
class CSVTableFormatter(TableFormatter):
    '''
    Выводит данные портфеля в формате CSV.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
```

Измените свою основную программу следующим образом:

```python
def portfolio_report(portfoliofile, pricefile):
    '''
    Создает отчет о портфеле по данным файлов портфеля и цен.
    '''
    # Читаем данные из файлов
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Создаем данные для отчета
    report = make_report_data(portfolio, prices)

    # Выводим их
    formatter = tableformat.CSVTableFormatter()
    print_report(report, formatter)
```

Теперь вы должны увидеть вывод в формате CSV, похожий на этот:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
```

С использованием аналогичной идеи определите класс `HTMLTableFormatter`, который выводит таблицу с таким выводом:

    <tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>
    <tr><td>AA</td><td>100</td><td>9.22</td><td>-22.98</td></tr>
    <tr><td>IBM</td><td>50</td><td>106.28</td><td>15.18</td></tr>
    <tr><td>CAT</td><td>150</td><td>35.46</td><td>-47.98</td></tr>
    <tr><td>MSFT</td><td>200</td><td>20.89</td><td>-30.34</td></tr>
    <tr><td>GE</td><td>95</td><td>13.48</td><td>-26.89</td></tr>
    <tr><td>MSFT</td><td>50</td><td>20.89</td><td>-44.21</td></tr>
    <tr><td>IBM</td><td>100</td><td>106.28</td><td>35.84</td></tr>

Проверьте свой код, изменив основную программу для создания объекта `HTMLTableFormatter` вместо объекта `CSVTableFormatter`.
