# Exercício 4.2: Adicionando alguns Métodos

Com classes, você pode anexar funções aos seus objetos. Estas são conhecidas como métodos e são funções que operam nos dados armazenados dentro de um objeto. Adicione um método `cost()` e `sell()` ao seu objeto `Stock`. Eles devem funcionar assim:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```
