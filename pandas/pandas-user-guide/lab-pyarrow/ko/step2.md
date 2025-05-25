# 데이터 구조 통합

PyArrow 를 사용하면 pandas 데이터 구조를 NumPy 배열과 유사하게 PyArrow ChunkedArray 로 직접 지원할 수 있습니다. 방법은 다음과 같습니다:

```python
# Import pandas
import pandas as pd

# Create a pandas Series, Index and DataFrame with PyArrow data type
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```
