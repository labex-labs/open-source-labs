# 创建并训练 MLP 模型

```python
# 创建一个具有 5 个神经元的单隐藏层 MLP 分类器
clf = MLPClassifier(hidden_layer_sizes=(5,), random_state=1)

# 使用训练数据训练模型
clf.fit(X, y)
```
