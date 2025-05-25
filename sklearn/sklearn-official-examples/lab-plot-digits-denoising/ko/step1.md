# OpenML 을 통해 데이터셋 로드

scikit-learn 의 `fetch_openml()` 함수를 사용하여 USPS 숫자 데이터셋을 로드합니다. 그런 다음 데이터를 `MinMaxScaler()`를 사용하여 정규화합니다.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
