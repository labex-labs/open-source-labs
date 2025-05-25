# 필요한 라이브러리 가져오기 및 DataFrame 생성

시작하려면 pandas 와 NumPy 와 같은 필요한 라이브러리를 가져와야 합니다. 그런 다음, 몇 가지 결측값이 있는 DataFrame 을 생성합니다.

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
