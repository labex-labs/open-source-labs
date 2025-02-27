# Загрузка набора данных через OpenML

Мы загружаем набор данных цифр USPS с использованием функции `fetch_openml()` из scikit-learn. Затем данные нормализуются с использованием `MinMaxScaler()`.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
