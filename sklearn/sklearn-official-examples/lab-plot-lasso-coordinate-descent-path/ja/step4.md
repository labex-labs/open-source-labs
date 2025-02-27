# エラスティックネットを使って正則化パスを計算する

このステップでは、エラスティックネット手法を使って正則化パスを計算し、matplotlibを使って結果を表示します。

```python
from sklearn.linear_model import enet_path

# エラスティックネットを使って正則化パスを計算する
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# matplotlibを使って結果を表示する
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("係数")
plt.title("エラスティックネットパス")
plt.axis("tight")
plt.show()
```
