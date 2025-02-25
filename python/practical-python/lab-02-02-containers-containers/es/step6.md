# Búsquedas en Diccionarios

Puedes probar la existencia de una clave.

```python
if key in d:
    # SI
else:
    # NO
```

Puedes buscar un valor que puede no existir y proporcionar un valor predeterminado en caso de que no exista.

```python
name = d.get(key, default)
```

Un ejemplo:

```python
>>> prices.get('IBM', 0.0)
93.37
>>> prices.get('SCOX', 0.0)
0.0
>>>
```
