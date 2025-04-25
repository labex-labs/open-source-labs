# 实现贝叶斯高斯混合模型

在这一步中，我们将使用 scikit-learn 的 `BayesianGaussianMixture` 类来实现贝叶斯高斯混合模型。该模型具有狄利克雷过程先验，它会根据数据自动调整聚类的数量。我们会将模型拟合到我们的数据集上，并预测每个数据点的聚类标签。最后，我们将绘制结果。

```python
# 创建一个具有 5 个组件的贝叶斯高斯混合模型对象
dpgmm = mixture.BayesianGaussianMixture(n_components=5, covariance_type="full")

# 将贝叶斯高斯混合模型拟合到数据上
dpgmm.fit(X)

# 预测聚类标签
Y_ = dpgmm.predict(X)

# 绘制结果
color_iter = ["navy", "c", "cornflowerblue", "gold", "darkorange"]

for i, color in enumerate(color_iter):
    plt.scatter(
        X[Y_ == i, 0], X[Y_ == i, 1], 0.8, color=color, label="Cluster {}".format(i)
    )

plt.legend(loc="best")
plt.title("具有狄利克雷过程先验的贝叶斯高斯混合模型")
plt.show()
```
