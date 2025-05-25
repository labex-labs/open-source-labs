# Formatação de Strings

Uma maneira de formatar strings no Python 3.6+ é com `f-strings`.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

A parte `{expressão:formato}` é substituída.

É comumente usado com `print`.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
