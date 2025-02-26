# Упражнение 7.4: Пропуск аргументов

Функция `fileparse.parse_csv()` имеет некоторые параметры для изменения разделителя файла и для отчета об ошибках. Возможно, вы хотите предоставить эти параметры для функции `read_portfolio()` выше. Примените следующие изменения:

    def read_portfolio(filename, **opts):
        '''
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

После внесения изменений попробуйте прочитать файл с некоторыми ошибками:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

Теперь, попробуйте подавить ошибки:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```
