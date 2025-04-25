# データセットの作成

2 つの多変量共分散 2 次元データセット X と Y を持つデータセットを作成します。その後、共分散の方向、つまり両データセット間で最も多くの共通分散を説明する各データセットのコンポーネントを抽出します。

```python
import numpy as np

n = 500
# 2 つの潜在変数：
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latents = np.array([l1, l1, l2, l2]).T
X = latents + np.random.normal(size=4 * n).reshape((n, 4))
Y = latents + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
