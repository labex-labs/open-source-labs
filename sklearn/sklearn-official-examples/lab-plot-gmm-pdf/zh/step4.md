# 绘制密度估计图

现在我们将绘制高斯混合的密度估计图。我们将在数据集的范围内创建一个点的网格，并计算GMM对每个点预测的负对数似然。然后，我们将把预测分数显示为等高线图，并将训练数据绘制成散点图。

```python
# 将模型预测的分数显示为等高线图
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Density Estimation with Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```
