# Data Structure Integration

PyArrow allows pandas data structures to be directly backed by a PyArrow ChunkedArray, similar to a NumPy array. Here is how to do this:

```python
# Import pandas
import pandas as pd

# Create a pandas Series, Index and DataFrame with PyArrow data type
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
