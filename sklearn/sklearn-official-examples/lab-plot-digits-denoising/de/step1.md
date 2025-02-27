# Lade den Datensatz über OpenML

Wir laden den USPS-Ziffern-Datensatz mit der Funktion `fetch_openml()` aus scikit-learn. Die Daten werden anschließend mithilfe von `MinMaxScaler()` normalisiert.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```
