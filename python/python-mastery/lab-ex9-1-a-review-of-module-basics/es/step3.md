# Carga repetida de módulos

Asegúrate de entender que los módulos solo se cargan una vez. Intenta una importación repetida y observa cómo no ves la salida de la función `print`:

```python
>>> import simplemod
>>>
```

Intenta cambiar el valor de `x` y observa que una importación repetida no tiene efecto.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> import simplemod
>>> simplemod.x
13
>>>
```

Utiliza `importlib.reload()` si quieres forzar la recarga de un módulo.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Cargado simplemod
<module'simplemod' from'simplemod.py'>
>>> simplemod.x
42
>>>
```

`sys.modules` es un diccionario de todos los módulos cargados. Echa un vistazo a él, elimina tu módulo y prueba una importación repetida.

```python
>>> sys.modules
... mira la salida...
>>> sys.modules['simplemod']
<module'simplemod' from'simplemod.py'>
>>> del sys.modules['simplemod']
>>> import simplemod
Cargado simplemod
>>>
```
