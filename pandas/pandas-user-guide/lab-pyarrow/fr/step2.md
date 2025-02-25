# Intégration des structures de données

PyArrow permet aux structures de données de pandas d'être directement prises en charge par un PyArrow ChunkedArray, similaire à un tableau NumPy. Voici comment faire :

```python
# Importez pandas
import pandas as pd

# Créez une série pandas, un index et un DataFrame avec un type de données PyArrow
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
