# Charger l'ensemble de données via OpenML

Nous chargeons l'ensemble de données de chiffres USPS à l'aide de la fonction `fetch_openml()` de scikit-learn. Les données sont ensuite normalisées à l'aide de `MinMaxScaler()`.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
