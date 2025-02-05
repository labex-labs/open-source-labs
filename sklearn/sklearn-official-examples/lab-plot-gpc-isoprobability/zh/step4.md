# 评估模型

我们将评估训练好的高斯过程分类（GPC）模型的分类性能。我们将生成一个点网格，并使用训练好的模型计算每个点的预测概率。

```python
# 评估真实函数和预测概率
res = 50
x1, x2 = np.meshgrid(np.linspace(-lim, lim, res), np.linspace(-lim, lim, res))
xx = np.vstack([x1.reshape(x1.size), x2.reshape(x2.size)]).T

y_true = g(xx)
y_prob = gp.predict_proba(xx)[:, 1]
y_true = y_true.reshape((res, res))
y_prob = y_prob.reshape((res, res))
```
