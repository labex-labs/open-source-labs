# 预测物种分布

在这一步中，我们将使用单类支持向量机（OneClassSVM）模型预测物种分布。我们将使用训练数据预测物种分布并绘制结果。

```python
# 使用训练数据预测物种分布
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# 我们仅对陆地点进行预测。
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# 绘制预测的等高线
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# 绘制训练/测试点的散点图
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```
