# Проблема

Предположим, что вы хотите создать собственный пользовательский паттерн итерации.

Например, обратный отсчет.

```python
>>> for x in countdown(10):
...   print(x, end=' ')
...
10 9 8 7 6 5 4 3 2 1
>>>
```

Есть простой способ сделать это.
