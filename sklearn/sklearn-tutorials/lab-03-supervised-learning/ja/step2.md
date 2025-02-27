# 線形回帰

このステップでは、線形回帰の概念と、scikit-learnを使ってそれを実装する方法を探ります。患者の生理的変数と1年後の病状進行からなる糖尿病データセットを使います。

#### 糖尿病データセットを読み込む

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### 線形回帰モデルを作成して適合させる

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### 予測を行い、性能指標を計算する

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
