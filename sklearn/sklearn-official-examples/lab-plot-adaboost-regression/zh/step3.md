# 绘制结果

最后，我们绘制我们的两个回归器，即单个决策树回归器和 AdaBoost 回归器，对数据的拟合程度。我们使用 Matplotlib 的 `scatter()` 函数来绘制训练样本以及两个回归器的预测值。我们使用 Matplotlib 的 `plot()` 函数来绘制两个回归器的预测值与数据的对比图。我们在图中添加一个图例以区分这两个回归器。

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Boosted Decision Tree Regression")
plt.legend()
plt.show()
```
