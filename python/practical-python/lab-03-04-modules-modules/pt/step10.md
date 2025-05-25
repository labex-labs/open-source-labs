# Localizando Módulos

Python consulta uma lista de caminhos (sys.path) ao procurar por módulos.

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

O diretório de trabalho atual geralmente é o primeiro.
