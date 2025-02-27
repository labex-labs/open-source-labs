# Cargar el conjunto de datos a través de OpenML

Cargamos el conjunto de datos de dígitos USPS utilizando la función `fetch_openml()` de scikit-learn. Los datos se normalizan luego utilizando `MinMaxScaler()`.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
