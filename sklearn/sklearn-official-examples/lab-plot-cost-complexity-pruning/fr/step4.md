# Entraîner les arbres de décision

Ensuite, nous allons entraîner un arbre de décision en utilisant chacune des valeurs d'alpha effectives. La dernière valeur de `ccp_alphas` est la valeur d'alpha qui taille l'arbre complet, laissant un arbre avec un seul nœud.

```python
clfs = []
for ccp_alpha in ccp_alphas:
    clf = DecisionTreeClassifier(random_state=0, ccp_alpha=ccp_alpha)
    clf.fit(X_train, y_train)
    clfs.append(clf)
print(
    "Nombre de nœuds dans le dernier arbre est : {} avec ccp_alpha : {}".format(
        clfs[-1].tree_.node_count, ccp_alphas[-1]
    )
)
```
