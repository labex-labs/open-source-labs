# Неизменяемость строк

Строки являются "неизменяемыми" или только для чтения. Как только они созданы, их значение нельзя изменить.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**Все операции и методы, которые манипулируют данными строк, всегда создают новые строки.**
