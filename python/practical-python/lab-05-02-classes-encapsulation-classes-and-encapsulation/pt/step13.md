# Exercício 5.7: Propriedades e Setters

Modifique o atributo `shares` para que o valor seja armazenado em um atributo privado e que um par de funções de propriedade seja usado para garantir que ele seja sempre definido como um valor inteiro. Aqui está um exemplo do comportamento esperado:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG',100,490.10)
>>> s.shares = 50
>>> s.shares = 'a lot'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected an integer
>>>
```
