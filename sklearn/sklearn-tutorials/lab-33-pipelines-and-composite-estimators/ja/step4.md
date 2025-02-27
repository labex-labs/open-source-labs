# 変換済みターゲット回帰器

`TransformedTargetRegressor` クラスは、回帰モデルを適合させる前に回帰問題のターゲット変数を変換するために使用されます。これは、対数を取るなど、ターゲット変数に変換を適用したい場合に便利です。予測は逆変換を介して元の空間にマッピングされます。以下は、線形回帰モデルと量子化変換器を使用した `TransformedTargetRegressor` の使用例です：

```python
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.compose import TransformedTargetRegressor
from sklearn.preprocessing import QuantileTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
transformer = QuantileTransformer(output_distribution='normal')
regressor = LinearRegression()
regr = TransformedTargetRegressor(regressor=regressor, transformer=transformer)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
regr.fit(X_train, y_train)
regr.score(X_test, y_test)
```
