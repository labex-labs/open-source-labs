# 필요한 라이브러리 가져오기 및 DataFrame 생성

먼저, 필요한 라이브러리를 가져오고 예제를 위한 DataFrame 을 생성해 보겠습니다.

```python
import pandas as pd
import numpy as np

# Create DataFrame
np.random.seed([3, 1415])
n = 20
cols = np.array(["key", "row", "item", "col"])
df = cols + pd.DataFrame((np.random.randint(5, size=(n, 4)) // [2, 1, 2, 1]).astype(str))
df.columns = cols
df = df.join(pd.DataFrame(np.random.rand(n, 2).round(2)).add_prefix("val"))
```
