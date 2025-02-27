# Обучение деревьев решений

Далее мы обучим дерево решений, используя каждое из эффективных значений альфа. Последнее значение в `ccp_alphas` - это значение альфа, которое усекает целое дерево, оставляя дерево с только одним узлом.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "Number of nodes in the last tree is: {} with ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
