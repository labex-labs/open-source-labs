# Возвращение нескольких значений

Предположим, что вы пишете код для разбора конфигурационных файлов, состоящих из строк такого вида:

    name=value

Напишите функцию `parse_line(line)`, которая принимает такую строку и возвращает как связанное имя, так и значение. Общий convention для возврата нескольких значений - это возвращать их в кортеже. Например:

```python
>>> parse_line('email=guido@python.org')
('email', 'guido@python.org')
>>> name, val = parse_line('email=guido@python.org')
>>> name
'email'
>>> val
'guido@python.org'
>>>
```
