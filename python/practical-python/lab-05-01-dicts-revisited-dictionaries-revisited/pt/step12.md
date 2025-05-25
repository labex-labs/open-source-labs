# Ordem de Resolução de Métodos ou MRO

O Python pré-calcula uma cadeia de herança e a armazena no atributo _MRO_ na classe. Você pode visualizá-la.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

Esta cadeia é chamada de **Ordem de Resolução de Métodos** (Method Resolution Order). Para encontrar um atributo, o Python percorre o MRO em ordem. A primeira correspondência vence.
