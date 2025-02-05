# 训练决策树

接下来，我们将使用每个有效α值训练一棵决策树。`ccp_alphas`中的最后一个值是修剪整个树的α值，这样树就只剩下一个节点。

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
