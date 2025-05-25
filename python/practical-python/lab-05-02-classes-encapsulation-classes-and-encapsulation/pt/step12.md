# Exercício 5.6: Propriedades Simples

Propriedades são uma maneira útil de adicionar "atributos computados" a um objeto. Em `stock.py`, você criou um objeto `Stock`. Observe que em seu objeto há uma ligeira inconsistência na forma como diferentes tipos de dados são extraídos:

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Especificamente, observe como você precisa adicionar os parênteses extras `()` a `cost` porque é um método.

Você pode se livrar dos parênteses extras `()` em `cost()` se o transformar em uma propriedade. Pegue sua classe `Stock` e modifique-a para que o cálculo do custo funcione assim:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Tente chamar `s.cost()` como uma função e observe que ela não funciona agora que `cost` foi definida como uma propriedade.

```python
>>> s.cost()
... fails ...
>>>
```

Fazer essa alteração provavelmente quebrará seu programa `pcost.py` anterior. Você pode precisar voltar e se livrar dos `()` no método `cost()`.
