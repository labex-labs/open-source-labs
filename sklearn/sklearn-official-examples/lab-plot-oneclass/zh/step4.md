# 可视化结果

最后，我们将可视化单类支持向量机模型的结果。我们将绘制决策边界、训练数据、常规新观测值和异常新观测值。

```python
# 可视化结果
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("异常检测")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors="darkred")
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors="palevioletred")

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c="white", s=s, edgecolors="k")
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c="blueviolet", s=s, edgecolors="k")
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c="gold", s=s, edgecolors="k")
plt.axis("tight")
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend(
    [a.collections[0], b1, b2, c],
    [
        "学习到的边界",
        "训练观测值",
        "新的常规观测值",
        "新的异常观测值"
    ],
    loc="upper left",
    prop=matplotlib.font_manager.FontProperties(size=11)
)
plt.xlabel(
    "训练错误：%d/200 ; 常规新观测值错误：%d/40 ; 异常新观测值错误：%d/40"
    % (n_error_train, n_error_test, n_error_outliers)
)
plt.show()
```

注：代码中的 `matplotlib.font_manager.FontProperties` 未翻译，因为它是 Python 中用于设置字体属性的类，保留英文更符合编程语境。
