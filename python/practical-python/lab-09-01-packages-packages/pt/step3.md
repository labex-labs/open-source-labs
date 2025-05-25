# Usando um Pacote (Package)

Um pacote serve como um namespace para imports.

Isso significa que agora existem imports de múltiplos níveis.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

Existem outras variações de declarações de import.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
