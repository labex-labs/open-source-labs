# Использование пакета

Пакет служит именнованным пространством для импортов.

Это означает, что теперь существуют импорты多层次。

```python
import porty.report
port = porty.report.read_portfolio('portfolio.csv')
```

Существуют и другие варианты инструкций import.

```python
from porty import report
port = report.read_portfolio('portfolio.csv')

from porty.report import read_portfolio
port = read_portfolio('portfolio.csv')
```
