# Excepciones revisadas

En los ejercicios, escribimos una función `parse()` que se parecía a esto:

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("No se pudo analizar :", line)
            print("Razón :", e)
    return records
```

Presta atención a la instrucción `try-except`. ¿Qué debes hacer en el bloque `except`?

¿Debes imprimir un mensaje de advertencia?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("No se pudo analizar :", line)
    print("Razón :", e)
```

¿O la ignoras en silencio?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Ninguna de las soluciones es satisfactoria porque a menudo se desea _ambas_ conductas (seleccionables por el usuario).
