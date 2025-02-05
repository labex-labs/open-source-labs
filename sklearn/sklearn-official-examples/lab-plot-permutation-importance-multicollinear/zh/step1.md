# 训练随机森林分类器

我们首先加载威斯康星乳腺癌数据集，并将其拆分为训练集和测试集。然后，我们在训练集上训练一个随机森林分类器，并在测试集上评估其准确率。

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Accuracy on test data: {:.2f}".format(clf.score(X_test, y_test)))
```
