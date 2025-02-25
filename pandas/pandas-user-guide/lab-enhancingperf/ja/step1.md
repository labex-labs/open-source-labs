# セットアップとサンプルデータの作成

始める前に、必要なモジュールをインポートしてサンプルのDataFrameを作成しましょう。

```python
# 必要なモジュールをインポート
import pandas as pd
import numpy as np

# サンプルのDataFrameを作成
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
