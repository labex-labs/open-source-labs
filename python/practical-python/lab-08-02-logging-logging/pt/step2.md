# Exceções Revisadas

Nos exercícios, escrevemos uma função `parse()` que se parecia com isto:

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
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

Concentre-se na instrução `try-except`. O que você deve fazer no bloco `except`?

Você deve imprimir uma mensagem de aviso?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

Ou você ignora silenciosamente?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

Nenhuma das soluções é satisfatória porque você frequentemente quer _ambos_ os comportamentos (selecionáveis pelo usuário).
