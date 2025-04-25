# OpenML を使ってデータセットを読み込む

scikit-learn の`fetch_openml()`関数を使って、USPS の数字データセットを読み込みます。その後、`MinMaxScaler()`を使ってデータを正規化します。

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
