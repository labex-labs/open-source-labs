# Exercício 5.4: Métodos vinculados (Bound methods)

Uma característica sutil do Python é que invocar um método realmente envolve duas etapas e algo conhecido como um método vinculado (bound method). Por exemplo:

```python
>>> s = goog.sell
>>> s
<bound method Stock.sell of Stock('GOOG', 100, 490.1)>
>>> s(25)
>>> goog.shares
75
>>>
```

Métodos vinculados (bound methods) realmente contêm todas as partes necessárias para chamar um método. Por exemplo, eles mantêm um registro da função que implementa o método:

```python
>>> s.__func__
<function sell at 0x10049af50>
>>>
```

Este é o mesmo valor encontrado no dicionário `Stock`.

```python
>>> Stock.__dict__['sell']
<function sell at 0x10049af50>
>>>
```

Métodos vinculados (bound methods) também registram a instância, que é o argumento `self`.

```python
>>> s.__self__
Stock('GOOG',75,490.1)
>>>
```

Quando você invoca a função usando `()`, todas as partes se juntam. Por exemplo, chamar `s(25)` realmente faz isso:

```python
>>> s.__func__(s.__self__, 25)    # Mesmo que s(25)
>>> goog.shares
50
>>>
```
