# Настройка и создание примера данных

Прежде чем мы начнем, импортируем необходимые модули и создадим пример DataFrame.

```python
# Import necessary modules
import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
