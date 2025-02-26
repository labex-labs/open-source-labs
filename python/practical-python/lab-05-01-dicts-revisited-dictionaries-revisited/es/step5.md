# Instancias y Clases

Las instancias y las clases están vinculadas. El atributo `__class__` se refiere a la clase.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{ 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s.__class__
<class '__main__.Stock'>
>>>
```

El diccionario de instancia contiene datos únicos para cada instancia, mientras que el diccionario de clase contiene datos compartidos colectivamente por _todas_ las instancias.
