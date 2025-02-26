# Упражнение 4.5: Проблема расширения

Предположим, что вы хотите изменить функцию `print_report()`, чтобы она поддерживала различные форматы вывода, такие как простой текст, HTML, CSV или XML. Для этого вы могли бы попробовать написать одну огромную функцию, которая делает все. Однако это, скорее всего, приведет к неуправляемой запутанной mess. Вместо этого это идеальный случай для использования наследования.

Для начала сосредоточьтесь на шагах, которые участвуют в создании таблицы. Вверху таблицы находится набор заголовков таблицы. Затем следуют строки с данными таблицы. Возьмем эти шаги и поместим их в собственный класс. Создайте файл под названием `tableformat.py` и определите следующий класс:

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Выводит заголовки таблицы.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Выводит одну строку с данными таблицы.
        '''
        raise NotImplementedError()
```

Этот класс ничего не делает, но он служит как определение для дополнительных классов, которые будут определены вскоре. Такой класс иногда называют "абстрактным базовым классом".

Измените функцию `print_report()`, чтобы она принимала объект `TableFormatter` в качестве входных данных и вызывала методы на нем для получения вывода. Например, так:

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Выводит красиво отформатированную таблицу из списка кортежей (имя, количество акций, цена, изменение).
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

Поскольку вы добавили аргумент в `print_report()`, вам также нужно изменить функцию `portfolio_report()`. Измените ее так, чтобы она создавала `TableFormatter` так:

```python
# report.py

import tableformat

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
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

Запустите этот новый код:

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... крашится...
```

Он должен немедленно завершиться с исключением `NotImplementedError`. Это не слишком захватывающее, но это именно то, что мы ожидали. Продолжайте дальше.
