# 帰納的学習モデルの宣言

このステップでは、未知のインスタンスのクラスタ所属を予測するために使用する帰納的学習モデルを宣言します。scikit - learnの`RandomForestClassifier`を分類器として使用します。

```python
classifier = RandomForestClassifier(random_state=42)
inductive_learner = InductiveClusterer(clusterer, classifier).fit(X)
```
