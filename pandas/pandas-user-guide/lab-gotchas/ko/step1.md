# DataFrame 메모리 사용량 이해

Pandas 는 DataFrame 의 메모리 사용량을 이해하기 위한 여러 가지 방법을 제공합니다. `.info()` 메서드를 사용하여 메모리 사용량을 포함한 요약을 확인할 수 있습니다.

```python
import pandas as pd
import numpy as np

# Create a DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Display DataFrame info
df.info()
```
