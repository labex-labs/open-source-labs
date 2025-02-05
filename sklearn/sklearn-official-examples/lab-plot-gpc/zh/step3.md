# 训练模型

我们将使用固定和优化后的超参数来训练高斯过程分类（GPC）模型。我们将打印模型的对数边缘似然、准确率和对数损失。

```python
# 固定超参数
gp_fix = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0), optimizer=None)
gp_fix.fit(X[:train_size], y[:train_size])

# 优化后的超参数
gp_opt = GaussianProcessClassifier(kernel=1.0 * RBF(length_scale=1.0))
gp_opt.fit(X[:train_size], y[:train_size])

# 结果
print("对数边缘似然（初始）: %.3f" % gp_fix.log_marginal_likelihood(gp_fix.kernel_.theta))
print("对数边缘似然（优化后）: %.3f" % gp_opt.log_marginal_likelihood(gp_opt.kernel_.theta))
print("准确率: %.3f（初始） %.3f（优化后）" % (accuracy_score(y[:train_size], gp_fix.predict(X[:train_size])), accuracy_score(y[:train_size], gp_opt.predict(X[:train_size]))))
print("对数损失: %.3f（初始） %.3f（优化后）" % (log_loss(y[:train_size], gp_fix.predict_proba(X[:train_size])[:, 1]), log_loss(y[:train_size], gp_opt.predict_proba(X[:train_size])[:, 1])))
```
