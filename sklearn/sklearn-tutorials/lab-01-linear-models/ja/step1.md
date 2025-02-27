# 最小二乗法

> 機械学習の経験がない場合は、[教師あり学習：回帰](https://labex.io/courses/supervised-learning-regression)から始めてください。

最小二乗法（OLS）は、観測されたターゲットと予測されたターゲットの二乗誤差の和を最小化する線形回帰手法です。数学的には、次の形式の問題を解きます。
$$\min_{w} || X w - y||_2^2$$

まず、OLS を使って線形回帰モデルをフィッティングしてみましょう。

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- scikit-learn から `linear_model` モジュールをインポートします。
- `LinearRegression` のインスタンスを作成します。
- `fit` メソッドを使ってモデルを訓練データにフィッティングします。
- 線形モデルの係数を表示します。
