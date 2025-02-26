# Упражнение 4.7: Полиморфизм на практике

Основной особенностью объектно-ориентированного программирования является то, что вы можете подключить объект к программе, и она будет работать, не требуя изменения существующего кода. Например, если вы написали программу, которая ожидает использовать объект `TableFormatter`, она будет работать независимо от того, какой именно `TableFormatter` вы ей на самом деле передадите. Это поведение иногда называется "полиморфизмом".

Одна потенциальная проблема заключается в том, как позволить пользователю выбрать форматтер, который он хочет. Прямое использование имен классов, таких как `TextTableFormatter`, часто раздражает. Таким образом, вы можете рассмотреть какой-то упрощенный подход. Возможно, вы внедрите `if`-условие в код, как это:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Создает отчет о портфеле по данным файлов портфеля и цен.
    '''
    # Читаем данные из файлов
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Создаем данные для отчета
    report = make_report_data(portfolio, prices)

    # Выводим их
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

В этом коде пользователь указывает упрощенное имя, такое как `'txt'` или `'csv'`, чтобы выбрать формат. Однако, является ли помещение большого `if`-условия в функцию `portfolio_report()` таким хорошим решением? Возможно, лучше перенести этот код в общую функцию в другом месте.

В файле `tableformat.py` добавьте функцию `create_formatter(name)`, которая позволяет пользователю создать форматтер, указав имя вывода, такое как `'txt'`, `'csv'` или `'html'`. Измените `portfolio_report()`, чтобы она выглядела так:

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Создает отчет о портфеле по данным файлов портфеля и цен.
    '''
    # Читаем данные из файлов
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Создаем данные для отчета
    report = make_report_data(portfolio, prices)

    # Выводим их
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

Попробуйте вызвать функцию с разными форматами, чтобы убедиться, что все работает.
