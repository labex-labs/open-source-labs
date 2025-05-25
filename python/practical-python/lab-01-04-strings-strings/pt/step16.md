# Exercício 1.17: f-strings

Às vezes, você quer criar uma string e embutir os valores de variáveis nela.

Para fazer isso, use uma f-string. Por exemplo:

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} shares of {name} at ${price:0.2f}'
'100 shares of IBM at $91.10'
>>>
```

Modifique o programa `mortgage.py` do Exercício 1.10 para criar sua saída usando f-strings. Tente fazer com que a saída seja bem alinhada.
