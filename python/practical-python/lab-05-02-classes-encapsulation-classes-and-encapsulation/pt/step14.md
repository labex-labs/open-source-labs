# Exercício 5.8: Adicionando slots

Modifique a classe `Stock` para que ela tenha um atributo `__slots__`. Em seguida, verifique se novos atributos não podem ser adicionados:

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.blah = 42
... see what happens ...
>>>
```

Quando você usa `__slots__`, Python usa uma representação interna mais eficiente de objetos. O que acontece se você tentar inspecionar o dicionário subjacente de `s` acima?

```python
>>> s.__dict__
... see what happens ...
>>>
```

Deve-se notar que `__slots__` é mais comumente usado como uma otimização em classes que servem como estruturas de dados. Usar slots fará com que esses programas usem muito menos memória e executem um pouco mais rápido. No entanto, você provavelmente deve evitar `__slots__` na maioria das outras classes.
