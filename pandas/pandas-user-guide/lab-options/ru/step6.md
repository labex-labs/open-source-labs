# Настройка параметров при запуске

Мы можем создать сценарий запуска в среде Python/IPython для импорта pandas и настройки параметров, что делает работу с pandas более эффективной.

```python
# This is an example of a startup script
# Place this in a.py file in the startup directory of IPython profile
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
