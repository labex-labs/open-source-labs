# Exemplo: Mantendo um Histórico

Problema: Queremos um histórico das últimas N coisas. Solução: Use um `deque`.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
        ...
```

O módulo `collections` pode ser um dos módulos de biblioteca mais úteis para lidar com tipos especiais de problemas de manipulação de dados, como tabulação e indexação.

Neste exercício, veremos alguns exemplos simples. Comece executando seu programa `report.py` para que você tenha o portfólio de ações carregado no modo interativo.

```bash
$ python3 -i report.py
```
