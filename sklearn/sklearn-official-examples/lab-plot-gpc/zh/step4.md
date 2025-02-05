# 绘制后验概率

我们将使用固定和优化后的超参数来绘制高斯过程分类（GPC）模型的后验概率。我们将绘制训练数据、测试数据以及类别1的预测概率。我们还将为这些图添加标签。

```python
# 绘制后验概率
plt.figure()
plt.scatter(X[:train_size, 0], y[:train_size], c="k", label="训练数据", edgecolors=(0, 0, 0))
plt.scatter(X[train_size:, 0], y[train_size:], c="g", label="测试数据", edgecolors=(0, 0, 0))
X_ = np.linspace(0, 5, 100)
plt.plot(X_, gp_fix.predict_proba(X_[:, np.newaxis])[:, 1], "r", label="初始核函数: %s" % gp_fix.kernel_)
plt.plot(X_, gp_opt.predict_proba(X_[:, np.newaxis])[:, 1], "b", label="优化后的核函数: %s" % gp_opt.kernel_)
plt.xlabel("特征")
plt.ylabel("类别1概率")
plt.xlim(0, 5)
plt.ylim(-0.25, 1.5)
plt.legend(loc="最佳位置")
```
