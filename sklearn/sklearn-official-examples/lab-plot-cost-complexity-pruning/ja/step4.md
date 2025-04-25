# 決定木を学習する

次に、それぞれの有効なアルファ値を使用して決定木を学習します。`ccp_alphas`の最後の値は、木全体を剪定し、1 つのノードだけの木にするアルファ値です。

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
