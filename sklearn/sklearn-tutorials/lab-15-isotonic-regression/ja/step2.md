# サンプルデータを作成する

次に、等張回帰モデルにフィットさせるためのサンプルデータを作成する必要があります。この例では、入力データとターゲット値をそれぞれ表す 2 つの配列`X`と`y`を生成します。

```python
import numpy as np

# Generate random input data
np.random.seed(0)
X = np.random.rand(100)
y = 4 * X + np.random.randn(100)
```
