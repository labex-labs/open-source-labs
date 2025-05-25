# 설정 및 샘플 데이터 생성

시작하기 전에, 필요한 모듈을 import 하고 샘플 DataFrame 을 생성해 보겠습니다.

```python
# Import necessary modules
import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
