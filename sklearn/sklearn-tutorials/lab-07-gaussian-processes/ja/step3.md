# ガウス過程分類（Gaussian Process Classification：GPC）

GaussianProcessClassifier クラスは、確率的分類に対して GPC を実装します。潜在関数に GP の事前分布を置き、それをリンク関数を通じてスカッシュ（圧縮）することでクラス確率を取得します。GPC は、one-versus-rest または one-versus-one に基づく学習と予測を行うことで多クラス分類をサポートします。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# RBF カーネルを持つ GPC モデルを作成する
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 学習データにモデルをフィッティングする
model.fit(X_train, y_train)

# 学習済みモデルを使って予測する
y_pred = model.predict(X_test)
```
