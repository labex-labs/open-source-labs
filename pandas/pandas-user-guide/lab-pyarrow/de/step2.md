# Integration von Datenstrukturen

PyArrow ermöglicht es, dass pandas-Datenstrukturen direkt von einem PyArrow-ChunkedArray unterstützt werden, ähnlich wie einem NumPy-Array. Hier ist, wie man dies macht:

```python
# Importiere pandas
import pandas as pd

# Erstelle eine pandas-Serie, -Index und -DataFrame mit PyArrow-Datentyp
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
