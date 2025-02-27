# モデルを学習する

次に、線形回帰オブジェクトを作成し、訓練セットを使ってモデルを学習します。

```python
from sklearn import linear_model

# 線形回帰オブジェクトを作成する
regr = linear_model.LinearRegression()

# 訓練セットを使ってモデルを学習する
regr.fit(diabetes_X_train, diabetes_y_train)
```
