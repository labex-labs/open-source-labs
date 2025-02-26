# Ejemplo: Conservar un historial

Problema: Queremos un historial de las últimas N cosas. Solución: Utiliza un `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
     ...
```

El módulo `collections` podría ser uno de los módulos de biblioteca más útiles para tratar problemas de manipulación de datos con fines especiales, como la tabulación e indexación.

En este ejercicio, veremos algunos ejemplos simples. Comience ejecutando su programa `report.py` para que tenga la cartera de acciones cargada en el modo interactivo.

```bash
$ python3 -i report.py
```
