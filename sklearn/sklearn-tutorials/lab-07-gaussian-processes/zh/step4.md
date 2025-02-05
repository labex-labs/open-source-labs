# GPC 示例

GPC 的概率预测：此示例展示了使用不同超参数选择时 GPC 的预测概率。

```python
# 创建一个具有 RBF 核的 GPC 模型
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 预测测试数据的类别概率
y_prob = model.predict_proba(X_test)
```

GPC 在异或数据集上的演示：此示例展示了 GPC 在异或数据集上的使用。我们比较了使用平稳、各向同性核（RBF）和非平稳核（DotProduct）的结果。

```python
# 创建具有不同核的 GPC 模型
各向同性核 = RBF(length_scale=1.0)
非平稳核 = DotProduct(sigma_0=1.0)

# 将模型拟合到异或数据集
各向同性模型 = GaussianProcessClassifier(kernel=各向同性核)
非平稳模型 = GaussianProcessClassifier(kernel=非平稳核)
各向同性模型.fit(X_xor, y_xor)
非平稳模型.fit(X_xor, y_xor)

# 使用训练好的模型进行预测
各向同性_y_pred = 各向同性模型.predict(X_test)
非平稳_y_pred = 非平稳模型.predict(X_test)
```

GPC 在鸢尾花数据集上的应用：此示例展示了使用各向同性 RBF 核和各向异性 RBF 核对鸢尾花数据集进行 GPC 的过程。它展示了不同超参数选择如何影响预测概率。

```python
# 创建具有不同核的 GPC 模型并将它们拟合到鸢尾花数据集
各向同性核 = RBF(length_scale=1.0)
各向异性核 = RBF(length_scale=[1.0, 2.0])
各向同性模型 = GaussianProcessClassifier(kernel=各向同性核)
各向异性模型 = GaussianProcessClassifier(kernel=各向异性核)
各向同性模型.fit(X_train, y_train)
各向异性模型.fit(X_train, y_train)

# 预测类别概率
各向同性_y_prob = 各向同性模型.predict_proba(X_test)
各向异性_y_prob = 各向异性模型.predict_proba(X_test)
```
