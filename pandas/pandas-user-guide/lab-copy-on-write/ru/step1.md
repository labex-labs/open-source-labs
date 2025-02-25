# Включение Copy-On-Write

Сначала давайте включим CoW в pandas. Это можно сделать с помощью параметра конфигурации `copy_on_write` в pandas. Вот два способа, с помощью которых можно включить CoW глобально.

```python
# Импортируем библиотеки pandas и numpy
import pandas as pd

# Включаем CoW с помощью set_option
pd.set_option("mode.copy_on_write", True)

# Или с помощью прямого назначения
pd.options.mode.copy_on_write = True
```
