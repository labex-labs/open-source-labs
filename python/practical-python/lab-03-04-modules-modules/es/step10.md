# Localización de módulos

Python consulta una lista de rutas (`sys.path`) cuando busca módulos.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
...
]
```

El directorio de trabajo actual suele estar primero.
