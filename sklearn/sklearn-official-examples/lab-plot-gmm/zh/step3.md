# 实现高斯混合模型

在这一步中，我们将使用 scikit-learn 的 `GaussianMixture` 类来实现高斯混合模型。我们会将模型拟合到我们的数据集上，并预测每个数据点的聚类标签。最后，我们将绘制结果。

```python
# 创建一个具有5个组件的高斯混合模型对象
gmm = mixture.GaussianMixture(n_components=5, covariance_type="full")

# 将高斯混合模型拟合到数据上
gmm.fit(X)

# 预测聚类标签
Y_ = gmm.predict(X)

# 绘制结果
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("高斯混合模型")
plt.show()
```
