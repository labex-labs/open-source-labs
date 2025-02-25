# Распаковка кортежа

Для использования кортежа в других местах можно распаковать его части в переменные.

```python
name, shares, price = s
print('Cost', shares * price)
```

Количество переменных слева должно соответствовать структуре кортежа.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
