# Entrenar los árboles de decisión

A continuación, entrenaremos un árbol de decisión utilizando cada uno de los valores efectivos de alfa. El último valor en `ccp_alphas` es el valor de alfa que poda el árbol completo, dejando un árbol con un solo nodo.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "Número de nodos en el último árbol es: {} con ccp_alpha: {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
