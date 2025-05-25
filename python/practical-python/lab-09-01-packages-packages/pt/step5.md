# Problema: Imports

Imports entre arquivos no mesmo pacote _agora devem incluir o nome do pacote no import_. Lembre-se da estrutura.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Exemplo de import modificado.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Todos os imports são _absolutos_, não relativos.

```python
import fileparse    # QUEBRA. fileparse não encontrado

...
```
