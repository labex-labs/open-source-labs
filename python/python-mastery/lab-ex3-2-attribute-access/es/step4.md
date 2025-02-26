# Métodos vinculados

Puede resultar sorprendente, pero las llamadas a métodos se superponen sobre la maquinaria utilizada para los atributos simples. Esencialmente, un método es un atributo que se ejecuta cuando se agregan los paréntesis () necesarios para llamarlo como una función. Por ejemplo:

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.cost           # Busca el método
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> s.cost()         # Busca y llama al método
49010.0

>>> # Mismas operaciones usando getattr()
>>> getattr(s, 'cost')
<bound method Stock.cost of <__main__.Stock object at 0x409530>>
>>> getattr(s, 'cost')()
49010.0
>>>
```

Un método vinculado está adjunto al objeto del que proviene. Si ese objeto se modifica, el método verá las modificaciones. Puede ver el objeto original inspeccionando el atributo `__self__` del método.

```python
>>> c = s.cost
>>> c()
49010.0
>>> s.shares = 75
>>> c()
36757.5
>>> c.__self__
<__main__.Stock object at 0x409530>
>>> c.__func__
<function cost at 0x37cc30>
>>> c.__func__(c.__self__)      # Esto es lo que sucede detrás de escena al llamar a c()
36757.5
>>>
```

Pruebe con el método `sell()` solo para asegurarse de entender el funcionamiento:

```python
>>> f = s.sell
>>> f.__func__(f.__self__, 25)     # Lo mismo que s.sell(25)
>>> s.shares
50
>>>
```
