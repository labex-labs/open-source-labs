# Verwendung eines Pakets

Ein Paket dient als Namensraum für Imports.

Dies bedeutet, dass es jetzt Mehr-Ebene-Imports gibt.

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

Es gibt auch andere Variationen von Importanweisungen.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
