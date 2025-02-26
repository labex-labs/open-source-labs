# Продолжайте

О, вы можете сделать лучше, чем это. Давайте внедрим это в ваш код генерации таблицы. Измените программу следующим образом:

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

Это должно произвести такой вывод:

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

Теперь, это просто бред! И очень круто.

**Обсуждение**

Некоторые уроки: вы можете создавать различные генераторные функции и связывать их вместе, чтобы выполнять обработку, связанную с конвейерами потока данных.

Хорошая модель для генераторных функций может быть乐高积木. Вы можете создать коллекцию небольших итераторных шаблонов и начать складывать их вместе различными способами. Это может быть чрезвычайно мощный способ программирования.
