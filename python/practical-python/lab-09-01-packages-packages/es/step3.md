# Usando un Paquete

Un paquete sirve como un espacio de nombres para las importaciones.

Esto significa que ahora hay importaciones de múltiples niveles.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

Hay otras variaciones de las declaraciones de importación.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
