# Integração da Estrutura de Dados

O PyArrow permite que as estruturas de dados do pandas sejam diretamente suportadas por um PyArrow ChunkedArray, semelhante a um array NumPy. Veja como fazer isso:

```python
# Import pandas
import pandas as pd

# Create a pandas Series, Index and DataFrame with PyArrow data type
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
