# Load the dataset via OpenML

We load the USPS digits dataset using `fetch_openml()` function from scikit-learn. The data is then normalized using `MinMaxScaler()`.

```python
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=41082, as_frame=False, return_X_y=True, parser="pandas")
X = MinMaxScaler().fit_transform(X)
```


