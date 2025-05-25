# Treinar as Árvores de Decisão

Em seguida, treinaremos uma árvore de decisão usando cada um dos valores de alpha efectivos. O último valor em `ccp_alphas` é o valor de alpha que poda toda a árvore, deixando a árvore apenas com um nó.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "Número de nós na última árvore é: {} com ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
