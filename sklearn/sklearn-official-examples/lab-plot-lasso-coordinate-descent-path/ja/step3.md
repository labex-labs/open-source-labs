# 正のラッソを使って正則化パスを計算する

このステップでは、正のラッソ手法を使って正則化パスを計算し、matplotlibを使って結果を表示します。

```python
# 正のラッソを使って正則化パスを計算する
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# matplotlibを使って結果を表示する
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("係数")
plt.title("ラッソと正のラッソ")
plt.legend((l1[-1], l2[-1]), ("ラッソ", "正のラッソ"), loc="lower left")
plt.axis("tight")
plt.show()
```
