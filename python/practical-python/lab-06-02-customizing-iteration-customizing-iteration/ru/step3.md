# Упражнение 6.4: Простой генератор

Если вы когда-нибудь будете хотеть настроить итерацию, вы должны всегда думать о генераторных функциях. Они легко писать - создайте функцию, которая реализует желаемую логику итерации, и используйте `yield` для выдачи значений.

Например, попробуйте этот генератор, который ищет в файле строки, содержащие заданную подстроку:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

Это довольно интересный подход - возможность скрыть сложную пользовательскую обработку в функции и использовать ее для заполнения цикла `for`. Следующий пример рассмотрит более необычный случай.
