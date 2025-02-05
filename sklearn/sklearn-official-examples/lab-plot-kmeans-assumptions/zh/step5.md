# 高斯混合模型

我们将探讨高斯混合模型的使用，它能够处理各向异性和方差不等的分布。在以下代码块中，我们使用 `GaussianMixture` 对第二个和第三个数据集进行聚类。

```python
from sklearn.mixture import GaussianMixture

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

y_pred = GaussianMixture(n_components=3).fit_predict(X_aniso)
ax1.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
ax1.set_title("各向异性分布的聚类")

y_pred = GaussianMixture(n_components=3).fit_predict(X_varied)
ax2.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
ax2.set_title("方差不等")

plt.suptitle("高斯混合聚类").set_y(0.95)
plt.show()
```
