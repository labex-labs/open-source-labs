# Imports Relativos

Em vez de usar diretamente o nome do pacote, você pode usar `.` para se referir ao pacote atual.

```python
from . import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Sintaxe:

```python
from . import modname
```

Isso facilita a renomeação do pacote.
