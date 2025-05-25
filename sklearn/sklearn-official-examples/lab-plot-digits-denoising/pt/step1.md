# Carregar o conjunto de dados através do OpenML

Carregamos o conjunto de dados de dígitos USPS usando a função `fetch_openml()` do scikit-learn. Os dados são então normalizados usando `MinMaxScaler()`.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
