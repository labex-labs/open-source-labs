# Упражнение 6.7: Мониторинг вашего портфеля

Измените программу `follow.py` так, чтобы она следила за потоком данных о акциях и выводила тикер, показывающий информацию только о тех акциях, которые находятся в портфеле. Например:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Примечание: Для того чтобы это работало, ваша класс `Portfolio` должен поддерживать оператор `in`. См. упражнение 6.3 и убедитесь, что вы реализуете оператор `__contains__()`.
