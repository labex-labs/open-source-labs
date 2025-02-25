# Импортируем необходимые библиотеки и создаем DataFrame

Для начала нам нужно импортировать необходимые библиотеки — pandas и NumPy. Затем мы создадим DataFrame с некоторыми пропущенными значениями.

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
