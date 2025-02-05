# 绘制等高线

我们绘制决策函数的等高线。首先，我们使用 `xx` 和 `yy` 数组创建一个网格。然后，我们将网格重塑为二维数组，并应用 `SVC` 类的 `decision_function` 方法来获取预测值。接着，我们使用 `contourf` 方法绘制等高线。

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
