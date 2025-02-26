# La línea `#!`

En Unix, la línea `#!` puede ejecutar un script como Python. Agregue lo siguiente a la primera línea de su archivo de script.

```python
#!/usr/bin/env python3
#./prog.py
...
```

Requiere permiso de ejecución.

```bash
$ chmod +x prog.py
# Luego puede ejecutar
$./prog.py
... salida...
```

_Nota: El lanzador de Python en Windows también busca la línea `#!` para indicar la versión del lenguaje._
