# Сравнения

Следующие операторы сравнения / отношения работают с числами:

    x < y      Менее чем
    x <= y     Менее или равно
    x > y      Больше чем
    x >= y     Больше или равно
    x == y     Равно
    x!= y     Не равно

Вы можете составлять более сложные булевы выражения, используя

`and`, `or`, `not`

Вот несколько примеров:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```
