# 声明归纳学习模型

在这一步中，我们将声明用于预测未知实例的聚类成员身份的归纳学习模型。我们将使用 scikit-learn 中的 `RandomForestClassifier` 作为分类器。

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```
