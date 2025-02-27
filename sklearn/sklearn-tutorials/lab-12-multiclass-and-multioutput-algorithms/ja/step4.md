# 多出力回帰

#### 問題の説明

多出力回帰は、各サンプルに対して複数の数値特性を予測します。各特性は数値変数であり、特性の数は 2 以上であることができます。

#### ターゲット形式

多出力回帰ターゲットの有効な表現は、密度行列で、各行がサンプルを表し、各列が異なる特性を表します。

#### 例

make_regression 関数を使って多出力回帰問題を作成しましょう。

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# Generate a multioutput regression problem
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# Fit a multioutput linear regression model
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```
