# La ruta de búsqueda de módulos

`sys.path` es un directorio que contiene la lista de todos los directorios revisados por la declaración `import`. Echa un vistazo:

```python
>>> import sys
>>> sys.path
... mira el resultado...
>>>
```

Si importas algo y no se encuentra en uno de esos directorios, obtendrás una excepción `ImportError`.
