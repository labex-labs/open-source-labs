# Менеджер контекста

В упражнении 3.5 вы сделали так, чтобы пользователи могли создавать красиво отформатированные таблицы. Например:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Одна проблема с этим кодом заключается в том, что все таблицы выводятся в стандартный вывод (`sys.stdout`). Предположим, что вы хотите перенаправить вывод в файл или в какое-то другое место. В общем случае вы могли бы изменить весь код форматирования таблиц, чтобы позволить использовать другой файл вывода. Однако, если нужно срочно, вы также можете решить эту проблему с помощью менеджера контекста.

Определите следующий менеджер контекста:

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

Этот менеджер контекста работает путём временного изменения `sys.stdout`, чтобы перенаправить весь вывод в другой файл. При выходе из контекста изменения отменяются. Попробуйте его:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # Проверьте файл
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
