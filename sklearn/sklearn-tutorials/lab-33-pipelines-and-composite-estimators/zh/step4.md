# 变换目标回归器

`TransformedTargetRegressor` 类用于在拟合回归模型之前对回归问题中的目标变量进行变换。当你想要对目标变量应用某种变换（例如取对数）时，这会很有用。预测结果会通过逆变换映射回原始空间。以下是一个将 `TransformedTargetRegressor` 与线性回归模型和分位数变换器一起使用的示例：

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
