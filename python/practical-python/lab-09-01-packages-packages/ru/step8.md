# Файлы `__init__.py`

Основная цель этих файлов - скрепить модули вместе.

Пример: объединение функций

```python
# porty/__init__.py
from.pcost import portfolio_cost
from.report import portfolio_report
```

Это позволяет именам появляться на _верхнем уровне_ при импорте.

```python
from porty import portfolio_cost
portfolio_cost('portfolio.csv')
```

Вместо использования многоуровневых импортов.

```python
from porty import pcost
pcost.portfolio_cost('portfolio.csv')
```
