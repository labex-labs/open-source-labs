# 通过 OpenML 加载数据集

我们使用 scikit-learn 中的 `fetch_openml()` 函数加载美国邮政服务（USPS）数字数据集。然后使用 `MinMaxScaler()` 对数据进行归一化处理。

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
