# 使用正弹性网络（Positive Elastic Net）计算正则化路径

在这一步中，我们将使用正弹性网络技术计算正则化路径，并使用matplotlib显示结果。

```python
# 使用正弹性网络计算正则化路径
alphas_positive_enet, coefs_positive_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8, positive=True)

# 使用matplotlib显示结果
plt.figure(4)
neg_log_alphas_positive_enet = -np.log10(alphas_positive_enet)
for coef_e, coef_pe, c in zip(coefs_enet, coefs_positive_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)
    l2 = plt.plot(neg_log_alphas_positive_enet, coef_pe, linestyle="--", c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("系数")
plt.title("弹性网络与正弹性网络")
plt.legend((l1[-1], l2[-1]), ("弹性网络", "正弹性网络"), loc="lower left")
plt.axis("tight")
plt.show()
```
