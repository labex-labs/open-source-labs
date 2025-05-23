# サンプルデータの生成

Scikit-learn の`make_regression()`関数を使ってサンプルデータを生成します。学習サンプル数を 75、テストサンプル数を 150、特徴数を 500 に設定します。また、`n_informative`を 50 に、`shuffle`を False に設定します。

```python
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

n_samples_train, n_samples_test, n_features = 75, 150, 500
X, y, coef = make_regression(
    n_samples=n_samples_train + n_samples_test,
    n_features=n_features,
    n_informative=50,
    shuffle=False,
    noise=1.0,
    coef=True,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_samples_train, test_size=n_samples_test, shuffle=False
)
```
