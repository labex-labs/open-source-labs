# 正のエラスティックネットを使って正則化パスを計算する

このステップでは、正のエラスティックネット手法を使って正則化パスを計算し、matplotlibを使って結果を表示します。

```python
# 正のエラスティックネットを使って正則化パスを計算する
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# matplotlibを使って結果を表示する
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("係数")
plt.title("エラスティックネットと正のエラスティックネット")
plt.legend((l1[-1], l2[-1]), ("エラスティックネット", "正のエラスティックネット"), loc="lower left")
plt.axis("tight")
plt.show()
```
