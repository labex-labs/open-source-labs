# Хранение текстовых данных

В pandas вы можете хранить текстовые данные двумя способами: с использованием NumPy-массива с типом `object` или расширения типа `StringDtype`. Мы рекомендуем использовать `StringDtype`, так как он безопаснее и более специфичен, чем общий тип `object`.

```python
import pandas as pd

# создать серию с типом `object`
s1 = pd.Series(["a", "b", "c"], dtype="object")

# создать серию с типом `StringDtype`
s2 = pd.Series(["a", "b", "c"], dtype="string")
```
