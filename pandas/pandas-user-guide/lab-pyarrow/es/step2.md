# Integración de Estructuras de Datos

PyArrow permite que las estructuras de datos de pandas estén directamente respaldadas por un PyArrow ChunkedArray, similar a una matriz de NumPy. Aquí está cómo hacerlo:

```python
# Importa pandas
import pandas as pd

# Crea una Serie, un Índice y un DataFrame de pandas con un tipo de datos de PyArrow
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
