# Leyendo Atributos

Supongamos que lees un atributo en una instancia.

```python
x = obj.name
```

El atributo puede existir en dos lugares:

- Diccionario local de instancia.
- Diccionario de clase.

Ambos diccionarios deben ser verificados. Primero, verifica en `__dict__` local. Si no se encuentra, busca en `__dict__` de la clase a través de `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Este esquema de búsqueda es cómo los miembros de una _clase_ se comparten entre todas las instancias.
