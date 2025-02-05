# 创建并训练决策树分类器

现在，我们可以使用训练数据创建并训练决策树分类器。

```python
# 创建一个决策树分类器
clf = tree.DecisionTreeClassifier()

# 训练分类器
clf.fit(X_train, y_train)
```
