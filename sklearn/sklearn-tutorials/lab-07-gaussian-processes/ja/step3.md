# ガウス過程分類（Gaussian Process Classification：GPC）

GaussianProcessClassifierクラスは、確率的分類に対してGPCを実装します。潜在関数にGPの事前分布を置き、それをリンク関数を通じてスカッシュ（圧縮）することでクラス確率を取得します。GPCは、one-versus-restまたはone-versus-oneに基づく学習と予測を行うことで多クラス分類をサポートします。

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# RBFカーネルを持つGPCモデルを作成する
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 学習データにモデルをフィッティングする
model.fit(X_train, y_train)

# 学習済みモデルを使って予測する
y_pred = model.predict(X_test)
```
