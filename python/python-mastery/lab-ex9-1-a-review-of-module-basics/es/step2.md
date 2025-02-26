# Carga de módulos y ruta del sistema

Intenta importar el módulo que acabas de crear:

```python
>>> import simplemod
Cargado simplemod
>>> simplemod.foo()
x es 42
>>>
```

Si esto falló con un `ImportError`, tu configuración de ruta está fallando. Mira el valor de `sys.path` y corrige it.

```python
>>> import sys
>>> sys.path
... mira el resultado...
>>>
```
