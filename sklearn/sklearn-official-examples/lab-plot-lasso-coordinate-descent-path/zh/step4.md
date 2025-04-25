# 使用弹性网络（Elastic Net）计算正则化路径

在这一步中，我们将使用弹性网络技术计算正则化路径，并使用 matplotlib 显示结果。

```python
from sklearn.linear_model import enet_path

# 使用弹性网络计算正则化路径
alphas_enet, coefs_enet, _ = enet_path(X, y, eps=eps, l1_ratio=0.8)

# 使用 matplotlib 显示结果
plt.figure(3)
neg_log_alphas_enet = -np.log10(alphas_enet)
for coef_e, c in zip(coefs_enet, colors):
    l1 = plt.plot(neg_log_alphas_enet, coef_e, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("系数")
plt.title("弹性网络路径")
plt.axis("tight")
plt.show()
```
