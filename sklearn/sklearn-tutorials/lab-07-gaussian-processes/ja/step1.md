# ガウス過程回帰（Gaussian Process Regression：GPR）

GaussianProcessRegressor クラスは、回帰タスクに対してガウス過程を実装します。GP の事前分布（prior）、たとえば平均関数と共分散関数を指定する必要があります。カーネルのハイパーパラメータは、フィッティング（適合）プロセス中に最適化されます。回帰に GPR を使用する例を見てみましょう。

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# RBF カーネルを持つ GPR モデルを作成する
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# 学習データにモデルをフィッティングする
model.fit(X_train, y_train)

# 学習済みモデルを使って予測する
y_pred = model.predict(X_test)
```
