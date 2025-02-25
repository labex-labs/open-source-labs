# Интеграция структур данных

PyArrow позволяет использовать структуры данных pandas, которые непосредственно основаны на PyArrow ChunkedArray, аналогично массиву NumPy. Вот, как это сделать:

```python
# Импортировать pandas
import pandas as pd

# Создать pandas Series, Index и DataFrame с типом данных PyArrow
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
