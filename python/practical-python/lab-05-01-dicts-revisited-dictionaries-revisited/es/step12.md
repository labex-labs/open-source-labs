# Orden de Resolución de Métodos o MRO

Python precomputa una cadena de herencia y la almacena en el atributo _MRO_ de la clase. Puedes verla.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

Esta cadena se llama **Orden de Resolución de Métodos**. Para encontrar un atributo, Python recorre el MRO en orden. La primera coincidencia gana.
