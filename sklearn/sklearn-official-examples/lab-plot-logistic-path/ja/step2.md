# 正則化パスを計算する

異なる正則化強度のL1ペナルティ付きロジスティック回帰モデルを学習することで正則化パスを計算します。L1ペナルティ付きのロジスティック回帰損失に対して効率的に最適化できるliblinearソルバーを使用します。係数を収集する前にモデルが収束していることを確認するために、許容誤差の低い値を設定します。また、warm_start=Trueを使用します。これは、モデルの係数を再利用して次のモデルのフィットを初期化し、フルパスの計算を高速化することを意味します。

```python
import numpy as np
from sklearn import linear_model
from sklearn.svm import l1_min_c

cs = l1_min_c(X, y, loss="log") * np.logspace(0, 10, 16)

clf = linear_model.LogisticRegression(
    penalty="l1",
    solver="liblinear",
    tol=1e-6,
    max_iter=int(1e6),
    warm_start=True,
    intercept_scaling=10000.0,
)
coefs_ = []
for c in cs:
    clf.set_params(C=c)
    clf.fit(X, y)
    coefs_.append(clf.coef_.ravel().copy())

coefs_ = np.array(coefs_)
```
