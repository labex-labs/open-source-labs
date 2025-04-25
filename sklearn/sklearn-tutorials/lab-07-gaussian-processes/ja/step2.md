# GPR の例

ノイズレベル推定付きの GPR：この例は、データのノイズレベルを推定するための WhiteKernel を含む和カーネルを持つ GPR を示しています。

```python
from sklearn.gaussian_process.kernels import WhiteKernel

# RBF カーネルと WhiteKernel を持つ GPR モデルを作成する
kernel = RBF() + WhiteKernel()
model = GaussianProcessRegressor(kernel=kernel)

# 学習データにモデルをフィッティングする
model.fit(X_train, y_train)

# 学習済みモデルを使って予測する
y_pred = model.predict(X_test)
```

GPR と Kernel Ridge 回帰の比較：Kernel Ridge 回帰（KRR）と GPR の両方は、「カーネルトリック」を使って目的関数を学習します。GPR は生成的な確率モデルを学習し、信頼区間を提供することができますが、KRR は予測のみを提供します。

```python
from sklearn.kernel_ridge import KernelRidge

# Kernel Ridge 回帰モデルを作成する
krr_model = KernelRidge(kernel='rbf')

# KRR モデルを学習データにフィッティングする
krr_model.fit(X_train, y_train)

# KRR モデルを使って予測する
krr_y_pred = krr_model.predict(X_test)

# 結果を GPR と比較する
gpr_model = GaussianProcessRegressor(kernel=RBF())
gpr_model.fit(X_train, y_train)
gpr_y_pred = gpr_model.predict(X_test)
```

モアナロアの CO2 データに対する GPR：この例は、対数尤度に対する勾配上昇を使った複雑なカーネルエンジニアリングとハイパーパラメータ最適化を示しています。データは、ハワイのモアナロア天文台で収集された月平均大気 CO2 濃度で構成されています。目的は、時間の関数として CO2 濃度をモデル化することです。

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

# 合成カーネルを持つ GPR モデルを作成する
kernel = 34.4**2 * RBF(length_scale=41.8) + 3.27**2 * RBF(length_scale=180) * ExpSineSquared(length_scale=1.44, periodicity=1) + 0.446**2 * RationalQuadratic(alpha=17.7, length_scale=0.957) + 0.197**2 * RBF(length_scale=0.138) + WhiteKernel(noise_level=0.0336)
model = GaussianProcessRegressor(kernel=kernel)

# データにモデルをフィッティングする
model.fit(X_train, y_train)

# 学習済みモデルを使って予測する
y_pred = model.predict(X_test)
```
