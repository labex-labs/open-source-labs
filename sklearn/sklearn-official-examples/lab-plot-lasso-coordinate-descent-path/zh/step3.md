# 使用正套索回归（Positive Lasso）计算正则化路径

在这一步中，我们将使用正套索回归技术计算正则化路径，并使用 matplotlib 显示结果。

```python
# 使用正套索回归计算正则化路径
alphas_positive_lasso, coefs_positive_lasso, _ = lasso_path(X, y, eps=eps, positive=True)

# 使用 matplotlib 显示结果
plt.figure(2)
neg_log_alphas_positive_lasso = -np.log10(alphas_positive_lasso)
for coef_l, coef_pl, c in zip(coefs_lasso, coefs_positive_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)
    l2 = plt.plot(neg_log_alphas_positive_lasso, coef_pl, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("系数")
plt.title("套索回归与正套索回归")
plt.legend((l1[-1], l2[-1]), ("套索回归", "正套索回归"), loc="lower left")
plt.axis("tight")
plt.show()
```
